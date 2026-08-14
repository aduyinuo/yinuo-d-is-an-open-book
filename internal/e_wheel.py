from envlib import *
# Cyberwheel: configurable env, blue deploys decoys, red spends its attack on one
REAL=[(1.7,3.55,"srv-a"),(1.7,2.65,"srv-b"),(1.7,1.75,"srv-c")]
DEC=[(4.4,3.55,"decoy-1"),(4.4,1.75,"decoy-2")]
CHAIN=["discovery","reconnaissance","privilege\nescalation","impact"]
CFG=[("network.yaml","hosts, subnets, services"),("host_types.yaml","what a host runs"),
     ("blue_agent.yaml","decoy types and cost"),("reward.yaml","what counts as a win"),
     ("observation","kill-chain, compact")]
steps=[]
for i in range(3): steps.append(("cfg",i))
steps+= [("decoy",0),("decoy",1)]
for i in range(4): steps.append(("red",i))
steps+= [("absorb",0),("absorb",1)]
frames=[]
for si,(kind,idx) in enumerate(steps):
    for k in range(4):
        f,ax=fig(9.0,4.0,10,4.5)
        txt(ax,0.15,4.30,"the network, the agents and the reward are all configuration",fs=9.0,c=D,ha="left")
        # config column
        ncfg = idx+1 if kind=="cfg" else len(CFG)
        for j,(nm,sub) in enumerate(CFG):
            on = j < (ncfg if kind=="cfg" else len(CFG))
            a = 1.0 if on else 0.25
            rbox(ax,1.15,3.55-j*0.62,2.0,0.5,c=M if on else L,fill=VL if on else "white",alpha=a)
            txt(ax,1.15,3.55-j*0.62+0.09,nm,fs=8.0,c=INK,a=a)
            txt(ax,1.15,3.55-j*0.62-0.13,sub,fs=6.8,c=MUTE,a=a)
        # network
        for (x,y,nm) in REAL:
            rbox(ax,x+2.6,y,1.35,0.48,c=M,fill="white")
            txt(ax,x+2.6,y,nm,fs=8.0,c=INK)
        shown_dec = (idx+1) if kind=="decoy" else (len(DEC) if si>4 else 0)
        for j,(x,y,nm) in enumerate(DEC):
            if j< shown_dec:
                gr = 1.0 if not (kind=="decoy" and j==idx) else (k+1)/4
                rbox(ax,x+2.6,y,1.35,0.48,c=OCH,fill=OCHL,alpha=gr)
                txt(ax,x+2.6,y,nm,fs=8.0,c=OCH,a=gr)
        # red progress along the chain
        prog = idx if kind=="red" else (4 if kind=="absorb" else 0)
        for j,st in enumerate(CHAIN):
            on = j<=prog and kind in ("red","absorb")
            x=3.35+j*1.62
            rbox(ax,x,0.52,1.45,0.5,c=D if on else L,fill="#dfeadf" if on else "white")
            txt(ax,x,0.52,st,fs=7.4,c=INK if on else MUTE)
            if j<3: ax.annotate("",xy=(x+0.86,0.52),xytext=(x+0.76,0.52),
                arrowprops=dict(arrowstyle="-|>",color=L,lw=1.2))
        if kind=="absorb":
            x,y,nm=DEC[1]
            ax.add_patch(FancyBboxPatch((x+2.6-0.72,y-0.28),1.44,0.56,boxstyle="round,pad=0.03,rounding_size=0.12",
                lw=2.6,ec=OCH,fc="none",alpha=0.35+0.65*(k+1)/4,zorder=6))
            txt(ax,8.35,2.72,"the attack lands on a decoy",fs=9.0,c=OCH,w="bold")
            txt(ax,8.35,2.42,"real hosts untouched; the red agent spent the episode",fs=7.6,c=MUTE)
        frames.append(f)
save(frames,"/tmp/anim/env-cyberwheel.gif",dur=95,hold=22)
