from envlib import *
TOOLS=[("nmap -sV 10.0.2.0/24","service versions, as the service reports them"),
       ("exploit against a live web service","it works or it doesn't"),
       ("meterpreter session opened","a real shell on a real host"),
       ("route add via session","pivot into the next segment"),
       ("credential dump","whatever is actually on disk")]
frames=[]
for si in range(len(TOOLS)+1):
    for k in range(5):
        f,ax=fig(9.2,4.0,10,4.5)
        txt(ax,0.15,4.34,"not a model of an attack — an attack, on provisioned infrastructure",fs=9.2,c=D,ha="left")
        # infrastructure
        txt(ax,1.6,3.92,"provisioned network",fs=8.4,c=MUTE)
        for j,(nm,sv) in enumerate([("host-01","web service"),("host-02","database"),("host-03","workstation")]):
            y=3.30-j*0.72
            owned = si>=2 and j==0 or si>=4 and j==1
            rbox(ax,1.6,y,2.2,0.6,c=D if owned else M,fill="#dfeadf" if owned else "white")
            txt(ax,1.6,y+0.10,nm,fs=8.2,c=INK); txt(ax,1.6,y-0.14,sv,fs=6.8,c=MUTE)
        # C2
        rbox(ax,4.15,3.30,1.9,0.6,c=OCH,fill=OCHL)
        txt(ax,4.15,3.30,"command & control",fs=8.0,c=OCH)
        if si>=3:
            a=0.25+0.75*abs(((k/5)*2)-1)
            ax.annotate("",xy=(3.15,3.30),xytext=(2.75,3.30),
                arrowprops=dict(arrowstyle="-|>",color=OCH,lw=1.8,alpha=a))
            txt(ax,2.95,3.62,"beacon",fs=7.0,c=OCH,a=a)
        # tool log
        txt(ax,5.45,3.92,"what the agent actually issues",fs=8.4,c=MUTE,ha="left")
        for j,(cmd,note) in enumerate(TOOLS):
            on=j<si
            y=3.50-j*0.50
            txt(ax,5.45,y,("$ "+cmd) if on else "",fs=7.9,c=INK,ha="left")
            txt(ax,5.45,y-0.18,note if on else "",fs=6.6,c=MUTE,ha="left")
        # cost counters
        txt(ax,0.15,0.62,"no abstract action space to argue about — the actions are tool invocations",fs=8.0,c=MUTE,ha="left")
        txt(ax,0.15,0.34,"no observation schema to align — what you see is whatever the system emits",fs=8.0,c=MUTE,ha="left")
        txt(ax,0.15,0.04,"and no millions of steps: setup is heavy, episodes are slow",fs=8.0,c=D,ha="left")
        frames.append(f)
save(frames,"/tmp/anim/env-daedelus.gif",dur=110,hold=18)
