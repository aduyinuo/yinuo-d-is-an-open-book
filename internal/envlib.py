import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle, Polygon
import numpy as np, io
from PIL import Image
INK="#1f2430"; MUTE="#8a9199"
D="#22452f"; M="#4a7c59"; L="#93b294"; VL="#e6efe4"; OFF="#eef2ee"; OCH="#a8843c"; OCHL="#e8dcc2"
DPI=125
def fig(w=8.0,h=3.6,xl=10,yl=4.5):
    f,ax=plt.subplots(figsize=(w,h),dpi=DPI)
    ax.set_xlim(0,xl); ax.set_ylim(0,yl); ax.axis("off"); f.patch.set_facecolor("white")
    return f,ax
def rbox(ax,x,y,w,h,c=M,fill=None,lw=1.4,alpha=1.0,z=3,r=0.10):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle=f"round,pad=0.02,rounding_size={r}",
        lw=lw,ec=c,fc=(fill if fill else "white"),alpha=alpha,zorder=z))
def txt(ax,x,y,s,fs=8.5,c=INK,ha="center",va="center",w=None,a=1.0,z=6,style=None):
    ax.text(x,y,s,fontsize=fs,color=c,ha=ha,va=va,weight=w,alpha=a,zorder=z,style=style)
def save(frames,out,dur=90,hold=20,loop=1):
    ims=[]
    for f in frames:
        b=io.BytesIO(); f.savefig(b,format="png",facecolor="white",bbox_inches="tight",pad_inches=0.12)
        plt.close(f); b.seek(0); im=Image.open(b).convert("RGB"); im.thumbnail((980,980),Image.LANCZOS)
        ims.append(im.convert("P",palette=Image.ADAPTIVE,colors=96))
    durs=[dur]*len(ims); durs[-1]=dur*hold
    ims[0].save(out,save_all=True,append_images=ims[1:],duration=durs,loop=loop,optimize=True,disposal=2)
    print(out,"frames",len(ims))
