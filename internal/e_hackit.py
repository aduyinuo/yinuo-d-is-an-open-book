from envlib import *
import numpy as np
# Two engagements on the same configured network: deception early vs deception late
np.random.seed(3)
HOSTS=[(0.9,3.05),(2.05,3.6),(2.05,2.5),(3.2,3.05),(0.9,1.6),(2.05,1.05),(3.2,1.6)]
HONEY={1,5}
def panel(ax,ox,title,path,revealed,step,note):
    txt(ax,ox+2.05,4.18,title,fs=9.6,c=D,w="bold")
    for i,(x,y) in enumerate(HOSTS):
        x=x+ox
        vis_h = i in HONEY and i in revealed
        c = OCH if vis_h else M
        fc = OCHL if vis_h else ("#dfeadf" if i in path[:step] else "white")
        ax.add_patch(Circle((x,y),0.28,fc=fc,ec=c,lw=1.6,zorder=3))
        txt(ax,x,y,f"h{i}",fs=7.6,c=INK if i in path[:step] else MUTE)
        if vis_h: txt(ax,x,y-0.46,"honeypot",fs=6.8,c=OCH)
    for a,b in [(0,1),(0,2),(1,3),(2,3),(0,4),(4,5),(5,6),(2,5),(3,6)]:
        (x1,y1),(x2,y2)=HOSTS[a],HOSTS[b]
        ax.plot([x1+ox,x2+ox],[y1,y2],color=L,lw=0.9,zorder=1,alpha=.85)
    for k in range(1,min(step,len(path))):
        (x1,y1),(x2,y2)=HOSTS[path[k-1]],HOSTS[path[k]]
        ax.annotate("",xy=(x2+ox,y2),xytext=(x1+ox,y1),
            arrowprops=dict(arrowstyle="-|>",color=D,lw=1.7,shrinkA=15,shrinkB=15),zorder=4)
    txt(ax,ox+0.1,0.30,f"round {min(step,len(path))}",fs=8.4,c=MUTE,ha="left")
    txt(ax,ox+0.1,0.02,note,fs=8.2,c=D,ha="left")
EARLY=[0,1,0,4,2,3,6]      # hits honeypot at round 2 -> spreads cautiously, verifies
LATE =[0,4,2,3,6,5,5]      # commits, hits honeypot late
notes_e=["probe the nearest server","fake ports, fake files — a honeypot","back off, re-probe elsewhere",
         "verify before committing","verify before committing","slow, sceptical, spread wide","slow, sceptical, spread wide"]
notes_l=["probe","move on, nothing suspicious yet","commit to a line of attack","commit to a line of attack",
         "deep in, still confident","the honeypot lands after the commitment","effort already spent"]
frames=[]
for step in range(0,8):
    for k in range(3):
        f,ax=fig(9.0,4.0,10,4.5)
        ax.plot([4.85,4.85],[0.5,3.95],color=L,lw=1.0,alpha=.6)
        rev_e={1} if step>=2 else set()
        rev_l={5} if step>=6 else set()
        panel(ax,0.35,"deception early",EARLY,rev_e,step,notes_e[min(step,6)])
        panel(ax,5.35,"deception late",LATE,rev_l,step,notes_l[min(step,6)])
        txt(ax,5.0,-0.34,"the same network, the same participant task — only the timing of the deception differs",fs=8.0,c=MUTE)
        frames.append(f)
save(frames,"/tmp/anim/env-hackit.gif",dur=110,hold=18)
