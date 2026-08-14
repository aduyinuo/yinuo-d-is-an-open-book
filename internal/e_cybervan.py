from envlib import *
import numpy as np
LEFT=[("VM · workstation","Windows, Office, browser",3.05),("VM · workstation","synthetic user at the keyboard",2.35),("VM · file server","SMB, real service stack",1.65)]
RIGHT=[("VM · mail server","SMTP, real stack",3.05),("VM · gateway","routing, DNS",2.35),("synthetic Internet","stand-in services and content",1.65)]
TAPS=[("packet capture","pcap and flow records"),("host logs","what the OS wrote down"),
      ("system calls","interception at the kernel boundary"),("user activity","window, mouse, keystroke, shell")]
frames=[]
NF=26
for t in range(NF):
    f,ax=fig(9.2,4.2,10,4.6)
    txt(ax,0.15,4.44,"real virtual machines, a simulated network between them",fs=9.2,c=D,ha="left")
    for nm,sub,y in LEFT:
        rbox(ax,1.35,y,2.3,0.66,c=M,fill="white"); txt(ax,1.35,y+0.11,nm,fs=8.0); txt(ax,1.35,y-0.14,sub,fs=6.7,c=MUTE)
    for nm,sub,y in RIGHT:
        rbox(ax,8.55,y,2.3,0.66,c=M,fill="white"); txt(ax,8.55,y+0.11,nm,fs=8.0); txt(ax,8.55,y-0.14,sub,fs=6.7,c=MUTE)
    # simulated core
    ax.add_patch(FancyBboxPatch((3.35,1.32),3.2,2.78,boxstyle="round,pad=0.06,rounding_size=0.25",
        lw=1.6,ec=OCH,fc=OCHL,alpha=.35,zorder=2))
    txt(ax,4.95,3.86,"discrete-event network simulator",fs=8.6,c=OCH,w="bold")
    txt(ax,4.95,3.62,"ns-3, with EMANE models",fs=7.4,c=MUTE)
    # links + moving packets (transparent forwarding)
    lanes=[(3.05,3.05),(2.35,2.35),(1.65,1.65)]
    for i,(yl,yr) in enumerate(lanes):
        ax.plot([2.52,3.35],[yl,yl],color=L,lw=1.1,zorder=1)
        ax.plot([6.55,7.38],[yr,yr],color=L,lw=1.1,zorder=1)
        ax.plot([3.5,6.4],[yl,yr],color=L,lw=0.9,ls=(0,(3,3)),zorder=3,alpha=.8)
        for j in range(3):
            p=((t/NF)+i*0.14+j*0.33)%1.0
            x=2.55+p*(7.35-2.55)
            y=yl
            ax.add_patch(Circle((x,y),0.055,fc=D,ec="none",zorder=5))
    txt(ax,4.95,1.10,"IP traffic forwarded transparently across the simulated segments",fs=7.2,c=MUTE)
    # instrumentation taps
    txt(ax,0.15,0.86,"because the hosts are real, the instrumentation is real",fs=8.4,c=D,ha="left")
    for j,(nm,sub) in enumerate(TAPS):
        x=1.35+j*2.42
        on = (t % NF) > j*3
        rbox(ax,x,0.36,2.26,0.52,c=M if on else L,fill=VL if on else "white",alpha=1 if on else .5)
        txt(ax,x,0.45,nm,fs=7.8,c=INK,a=1 if on else .5)
        txt(ax,x,0.24,sub,fs=6.3,c=MUTE,a=1 if on else .5)
    frames.append(f)
save(frames,"/tmp/anim/env-cybervan.gif",dur=95,hold=16,loop=0)
