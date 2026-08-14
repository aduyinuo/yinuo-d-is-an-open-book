from envlib import *
import numpy as np
np.random.seed(11)
NODES={"web":(1.15,3.25),"file":(2.45,3.80),"dev":(2.45,2.70),"db":(3.75,3.25),"admin":(5.05,3.80),"vault":(5.05,2.70)}
EDGES=[("web","file"),("web","dev"),("file","db"),("dev","db"),("db","admin"),("db","vault")]
CHAIN=["web","dev","db","vault"]
frames=[]
def base(ax,lit=(),arrow=0):
    txt(ax,0.15,4.30,"an enterprise network as a graph — with a very large way of describing a move",fs=9.0,c=D,ha="left")
    for a,b in EDGES:
        (x1,y1),(x2,y2)=NODES[a],NODES[b]
        ax.plot([x1,x2],[y1,y2],color=L,lw=1.0,zorder=1)
    for n,(x,y) in NODES.items():
        on=n in lit
        ax.add_patch(Circle((x,y),0.33,fc="#dfeadf" if on else "white",ec=D if on else M,lw=1.7,zorder=3))
        txt(ax,x,y,n,fs=7.8,c=INK if on else MUTE)
    for k in range(1,arrow):
        (x1,y1),(x2,y2)=NODES[CHAIN[k-1]],NODES[CHAIN[k]]
        ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="-|>",color=D,lw=1.8,shrinkA=18,shrinkB=18),zorder=4)
# phase 1: the action space blows up
for i in range(10):
    f,ax=fig(9.0,4.0,10,4.5)
    base(ax)
    n=10**(1+i*1.0)
    ax.plot([6.35,6.35],[2.35,4.05],color=L,lw=1.0,alpha=.7)
    txt(ax,8.2,3.92,"action = (source, target, vulnerability)",fs=8.2,c=MUTE)
    txt(ax,8.2,3.40,f"{n:,.0f}".replace(","," ") if n<1e6 else f"10^{1+i}",fs=17,c=D,w="bold")
    txt(ax,8.2,3.00,"candidate triples",fs=8.0,c=MUTE)
    # observation strip
    txt(ax,0.15,1.95,"observation — 512 dimensions, weakly structured",fs=8.4,c=MUTE,ha="left")
    rel=set(np.random.choice(512,26,replace=False))
    for j in range(512):
        cx=0.18+(j%64)*0.152; cy=1.62-(j//64)*0.135
        ax.add_patch(Rectangle((cx,cy),0.115,0.10,fc=(D if j in rel else OFF),ec="none",zorder=3))
    txt(ax,0.15,0.42,"only a small fraction of the features bear on the decision at hand",fs=8.0,c=MUTE,ha="left")
    txt(ax,0.15,0.12,"which is why training here is sample-inefficient",fs=8.0,c=D,ha="left")
    frames.append(f)
# phase 2: short horizon once a policy exists
for step in range(1,6):
    for k in range(3):
        f,ax=fig(9.0,4.0,10,4.5)
        base(ax,lit=CHAIN[:min(step,4)],arrow=min(step,4))
        ax.plot([6.35,6.35],[2.35,4.05],color=L,lw=1.0,alpha=.7)
        txt(ax,8.2,3.92,"once a policy exists",fs=8.2,c=MUTE)
        txt(ax,8.2,3.40,f"{min(step,4)-1} / 3",fs=17,c=D,w="bold")
        txt(ax,8.2,3.00,"steps used",fs=8.0,c=MUTE)
        txt(ax,0.15,1.95,"discovery is supplied; the credential chain is short",fs=8.4,c=MUTE,ha="left")
        for j in range(512):
            cx=0.18+(j%64)*0.152; cy=1.62-(j//64)*0.135
            ax.add_patch(Rectangle((cx,cy),0.115,0.10,fc=OFF,ec="none",zorder=3))
        txt(ax,0.15,0.42,"a hard search problem with an easy task horizon",fs=8.0,c=MUTE,ha="left")
        txt(ax,0.15,0.12,"for transfer work it is the far target: action spaces align only partly",fs=8.0,c=D,ha="left")
        frames.append(f)
save(frames,"/tmp/anim/env-cyberbattle.gif",dur=120,hold=18)
