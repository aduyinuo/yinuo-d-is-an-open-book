import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
D="#22452f"; M="#4a7c59"; L="#93b294"; VL="#e6efe4"; OFF="#dfe6df"; INK="#1f2430"; MUTE="#8a9199"
rows=[("Cyber World Modeling",["FOE-Dreamer","Learn Structure"]),
      ("Mental World Modeling",["Problem-Solving","Opponent Modeling"]),
      ("Human-AI Complementarity",["CHART","Team Defense Game","CyberAgentTrace"]),
      ("Toward Deployment",["Metrion","Transfer","Environments"])]
cols=["read","model","build","run","write","review","teach"]
# marks: (thread, activity) -> weight 0..1  (only where a public artifact exists)
mk={("FOE-Dreamer","model"):1,("FOE-Dreamer","build"):.7,("FOE-Dreamer","write"):1,("FOE-Dreamer","review"):1,
    ("Learn Structure","read"):.7,("Learn Structure","model"):1,("Learn Structure","write"):.7,
    ("Problem-Solving","read"):.7,("Problem-Solving","run"):1,("Problem-Solving","build"):1,("Problem-Solving","write"):1,
    ("Opponent Modeling","model"):1,("Opponent Modeling","run"):.7,("Opponent Modeling","write"):1,("Opponent Modeling","review"):.7,
    ("CHART","build"):1,("CHART","write"):1,
    ("Team Defense Game","run"):1,("Team Defense Game","write"):1,("Team Defense Game","teach"):.5,
    ("CyberAgentTrace","build"):1,("CyberAgentTrace","run"):.7,("CyberAgentTrace","write"):1,
    ("Metrion","read"):1,("Metrion","write"):1,("Metrion","review"):.5,
    ("Transfer","model"):1,("Transfer","run"):1,("Transfer","write"):1,
    ("Environments","read"):1,("Environments","run"):.7}
threads=[t for _,ts in rows for t in ts]
n=len(threads); m=len(cols)
y={}; pos=0.0; gaps=[]
seq=[]
for gi,(grp,ts) in enumerate(rows):
    if gi: pos+=0.45
    ys=[]
    for t in ts:
        seq.append((t,pos)); ys.append(pos); pos+=1.0
    gaps.append((grp,ys))
top=pos-1.0
for t,p in seq: y[t]=top-p+0.0
y={t: (pos-1.0-p) for t,p in seq}
N=pos-1.0
fig,ax=plt.subplots(figsize=(9.4,6.0),dpi=170)
ax.set_xlim(-5.6,m+0.4); ax.set_ylim(-1.6,N+1.2); ax.axis("off")
for j,c in enumerate(cols):
    ax.text(j+0.5,N+1.05,c,ha="center",va="bottom",fontsize=9,color=MUTE,family="DejaVu Sans")
for grp,ts in rows:
    ys=[y[t] for t in ts]
    lbl=grp.replace(" World ","\nWorld ").replace("Human-AI ","Human-AI\n").replace("Toward ","Toward\n")
    ax.text(-5.5,(max(ys)+min(ys))/2+0.5,lbl,ha="left",va="center",fontsize=9.5,color=D,weight="bold",linespacing=1.35)
    ax.plot([-0.45,-0.45],[min(ys)+0.05,max(ys)+0.95],color=L,lw=2.4,solid_capstyle="round")
for t in threads:
    ax.text(-0.65,y[t]+0.5,t,ha="right",va="center",fontsize=9,color=INK)
    for j,c in enumerate(cols):
        w=mk.get((t,c),0)
        col= D if w>=1 else (M if w>=.7 else (L if w>0 else OFF))
        a = 1 if w>0 else .55
        ax.add_patch(FancyBboxPatch((j+0.12,y[t]+0.12),0.76,0.76,
            boxstyle="round,pad=0,rounding_size=0.14",fc=col,ec="none",alpha=a))
ax.text(-5.5,-0.95,"filled where the thread has left a public artifact — a paper, a tool, a page",
        fontsize=8.2,color=MUTE,ha="left",va="center")
plt.tight_layout()
fig.savefig("/tmp/anim/activity-board.png",transparent=True,bbox_inches="tight",pad_inches=0.15)
print("ok")
