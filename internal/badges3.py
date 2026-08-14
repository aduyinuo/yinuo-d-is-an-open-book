from PIL import Image, ImageDraw, ImageFont
import os
S=3
GREEN=(74,124,89)
FW=96          # fixed final width (px)
PADX=7         # inner horizontal padding (final px)
LH=13          # line height (final px)
VPAD=5         # top/bottom padding (final px)
FS=10          # font size (final px)
def font(sz):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
F=font(FS*S)
_tmp=ImageDraw.Draw(Image.new("RGBA",(10,10)))
def tw(s):
    l,t,r,b=_tmp.textbbox((0,0),s,font=F); return (r-l)/S
def wrap(text):
    maxw=FW-2*PADX
    words=text.split(" "); lines=[]; cur=""
    for w in words:
        cand=(cur+" "+w).strip()
        if tw(cand)<=maxw or not cur: cur=cand
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    # hard-split any single word still too wide
    out=[]
    for ln in lines:
        while tw(ln)>maxw and len(ln)>1:
            lo=1
            while lo<len(ln) and tw(ln[:lo+1])<=maxw: lo+=1
            out.append(ln[:lo]); ln=ln[lo:]
        out.append(ln)
    return out
def badge(text,out,c=GREEN):
    lines=wrap(text)
    W=FW*S; H=(2*VPAD+LH*len(lines))*S
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,W-1,H-1],radius=int(H/2 if len(lines)==1 else 8*S),
        fill=c+(30,),outline=c+(180,),width=max(1,int(1.3*S)))
    for i,ln in enumerate(lines):
        l,t,r,b=d.textbbox((0,0),ln,font=F); w=r-l
        x=(W-w)/2-l; y=(VPAD+LH*i)*S - t + (LH*S-(b-t))/2
        d.text((x,y),ln,font=F,fill=c+(255,))
    im.resize((FW,H//S),Image.LANCZOS).save(out)

VENUE=[("RAISE-EROCIS","badge-raise2"),("AAAI-Summer Symposium","badge-aaai"),
   ("AAAI Symposium","badge-aaaiss"),("Collective Intelligence","badge-ci"),("Book","badge-book"),
   ("CHB: AI","badge-chb"),("ACM TSC","badge-tsc"),("Acta Psych.","badge-acta"),("CogSci","badge-cogsci"),
   ("Empirical","badge-empirical"),("J. Cybersec.","badge-jcyb"),("HCOMP","badge-hcomp"),("HFES","badge-hfes"),
   ("OptLearnMAS","badge-aamas"),("arXiv","badge-arxiv"),("Preprint","badge-preprint"),
   ("ACM CCS","badge-ccs"),("SIGCSE","badge-sigcse"),("GameSec","badge-gamesec")]
for t,n in VENUE: badge(t,n+".png")
print("venue badges rebuilt at fixed width", FW)
