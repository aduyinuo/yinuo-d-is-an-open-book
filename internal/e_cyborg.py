from envlib import *
# CAGE Challenge 2 topology, reward accrual, restoring defender
users=[("User0",0),("User1",1),("User2",2),("User3",3),("User4",4)]
ent=[("Enterprise0",0),("Enterprise1",1),("Enterprise2",2),("Defender",3)]
op=[("Op_Host0",0),("Op_Host1",1),("Op_Host2",2),("Op_Server0",3)]
COLS={"u":1.45,"e":4.6,"o":7.9}
def ypos(i,n): return 3.55-i*0.62
POS={}
for n,i in users: POS[n]=(COLS["u"],ypos(i,5))
for n,i in ent: POS[n]=(COLS["e"],ypos(i,4))
for n,i in op: POS[n]=(COLS["o"],ypos(i,4))
# script: (host owned, reward add, note)
script=[("User0",0.0,"permanent foothold on User0"),
        ("User1",0.1,"lateral movement inside the user subnet"),
        ("Enterprise1",1.0,"the enterprise layer is a mandatory waypoint"),
        ("Enterprise2",1.0,"the operational subnet is not reachable directly"),
        ("Op_Host1",1.0,"into the operational subnet"),
        ("Op_Server0",1.0,"Op_Server0 held"),
        ("IMPACT",10.0,"Impact on Op_Server0 pays 10.0"),
        ("RESTORE",0.0,"the restoring defender puts a host back to clean")]
frames=[]
owned=[]; reward=0.0; restored=None
steps=[]
for si,(h,r,note) in enumerate(script):
    for k in range(6):
        f,ax=fig(8.6,3.9,10,4.5)
        # subnet panels
        for key,lab,cnt in [("u","user subnet",5),("e","enterprise subnet",4),("o","operational subnet",4)]:
            x=COLS[key]
            ax.add_patch(FancyBboxPatch((x-1.05,ypos(cnt-1,cnt)-0.34),2.1,0.62*cnt+0.06,
                boxstyle="round,pad=0.06,rounding_size=0.12",lw=0,fc=VL,alpha=.55,zorder=1))
            txt(ax,x,3.55+0.55,lab,fs=8.6,c=D,w="bold")
        # links between subnets
        for a,b in [(("User1"),("Enterprise1")),(("User3"),("Enterprise0")),(("Enterprise2"),("Op_Host1")),(("Enterprise1"),("Op_Host0"))]:
            (x1,y1),(x2,y2)=POS[a],POS[b]
            ax.plot([x1+1.0,x2-1.0],[y1,y2],color=L,lw=1.0,zorder=1,alpha=.9)
        cur_owned=list(owned)
        if h not in ("IMPACT","RESTORE"): cur_owned=owned+[h]
        restored = "Enterprise1" if (h=="RESTORE" and k>=1) else None
        if restored: cur_owned=[o for o in cur_owned if o!="Enterprise1"]
        for name,(x,y) in POS.items():
            is_own = name in cur_owned and not (restored==name)
            c = D if is_own else M
            fc = "#dfeadf" if is_own else "white"
            if name=="Defender": c,fc=OCH,("#f6efe0")
            rbox(ax,x,y,1.9,0.46,c=c,fill=fc,lw=1.6 if is_own else 1.1)
            txt(ax,x,y,name,fs=8.0,c=INK if is_own else MUTE,w="bold" if is_own else None)
            if name=="Op_Server0" and h=="IMPACT":
                a=0.25+0.75*(k/5)
                ax.add_patch(FancyBboxPatch((x-1.02,y-0.27),2.04,0.54,boxstyle="round,pad=0.03,rounding_size=0.12",
                    lw=2.4,ec=OCH,fc="none",alpha=a,zorder=5))
            if restored==name:
                ax.add_patch(FancyBboxPatch((x-1.02,y-0.27),2.04,0.54,boxstyle="round,pad=0.03,rounding_size=0.12",
                    lw=2.2,ec=OCH,fc="none",alpha=1,zorder=5))
        # reward meter
        shown = reward + (r*(k+1)/6 if r else 0)
        txt(ax,0.15,0.42,"cumulative reward to the attacker",fs=8.2,c=MUTE,ha="left")
        txt(ax,0.15,0.10,f"{shown:5.1f}",fs=15,c=D,ha="left",w="bold")
        bw=min(shown/15.0,1.0)*6.4
        ax.add_patch(FancyBboxPatch((1.4,0.06),6.4,0.16,boxstyle="round,pad=0,rounding_size=0.08",lw=0,fc=OFF,zorder=2))
        if bw>0.02: ax.add_patch(FancyBboxPatch((1.4,0.06),bw,0.16,boxstyle="round,pad=0,rounding_size=0.08",lw=0,fc=M,zorder=3))
        txt(ax,9.85,0.42,"user 0.1 · server 1.0 · impact 10.0",fs=7.6,c=MUTE,ha="right")
        txt(ax,0.15,4.32,note,fs=9.0,c=D,ha="left")
        frames.append(f)
    if h=="RESTORE":
        owned=[o for o in owned if o!="Enterprise1"]
    elif h!="IMPACT":
        owned.append(h)
    reward+=r
save(frames,"/tmp/anim/env-cyborg.gif",dur=95,hold=22)
