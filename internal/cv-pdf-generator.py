from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                               TableStyle, HRFlowable)

DARK = colors.HexColor("#22452f")
INK  = colors.HexColor("#1f2430")
MUTE = colors.HexColor("#6b7280")

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, leading=23,
                      textColor=DARK, spaceAfter=2)
role = ParagraphStyle("role", fontName="Helvetica", fontSize=10.5, leading=14,
                      textColor=INK, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.8, leading=12,
                         textColor=MUTE, spaceAfter=10)
h = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
                   textColor=DARK, spaceBefore=11, spaceAfter=4)
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=9, leading=12.2, textColor=INK)
yr   = ParagraphStyle("yr", fontName="Helvetica-Bold", fontSize=9, leading=12.2, textColor=DARK)
note = ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.2, leading=11,
                      textColor=MUTE, spaceBefore=8)

def P(t, s=cell): return Paragraph(t, s)

def section(title, rows, w0=1.05):
    out = [Paragraph(title, h),
           HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#c8d6c8"),
                      spaceBefore=1, spaceAfter=5)]
    data = [[P(a, yr), P(b)] for a, b in rows]
    t = Table(data, colWidths=[w0*inch, (6.9-w0)*inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 1.5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4.5),
    ]))
    out.append(t)
    return out

doc = SimpleDocTemplate(
    "/sessions/festive-hopeful-edison/mnt/GitHub/content/.gitbook/assets/yinuo-du-cv.pdf",
    pagesize=LETTER, leftMargin=0.8*inch, rightMargin=0.8*inch,
    topMargin=0.7*inch, bottomMargin=0.7*inch,
    title="Yinuo Du - Curriculum Vitae", author="Yinuo Du")

s = []
s.append(Paragraph("Yinuo Du", name))
s.append(Paragraph("Assistant Professor of Research, Computer Science, University of Texas at El Paso", role))
s.append(Paragraph(
    'Google Scholar: scholar.google.com/citations?user=XdY3VB0AAAAJ &nbsp;·&nbsp; '
    'LinkedIn: linkedin.com/in/yinuo-du', contact))

s += section("Academic employment", [
    ("2025 (– 2026)", "Assistant Professor of Research, Computer Science Department, University of Texas at El Paso"),
])

s += section("Education", [
    ("2021 – 2025", "PhD, Societal Computing, School of Computer Science, Carnegie Mellon University<br/>"
                    "<i>Thesis:</i> Human and AI Decision-Making in Cybersecurity: A Multiagent Modeling Perspective<br/>"
                    "<i>Advisors:</i> Cleotilde Gonzalez, Fei Fang<br/>"
                    "<i>Committee:</i> Cleotilde Gonzalez, Fei Fang, Christian Lebiere, Prashanth Rajivan, Tiffany Bao"),
    ("2019 – 2021", "MSc, Information Technology, Information Networking Institute, Carnegie Mellon University"),
    ("2015 – 2019", "BS, Software Engineering, Xi'an Jiaotong University"),
])

s += section("Honors and awards", [
    ("2026", "University Research Institute (URI) award, University of Texas at El Paso"),
    ("2025", "SCS Presidential Fellowship, Carnegie Mellon University"),
    ("2023 – 2024", "Women in Cybersecurity Student Scholarship"),
    ("2023", "Accelerating Foundation Models Research (PI: Cleotilde Gonzalez)"),
    ("2018", "Foho Technical Innovation Grant — 1 of 77 awarded"),
    ("2016 – 2018", "National Encouragement Scholarship, Xi'an Jiaotong University — 3 of 77 awarded"),
])

s += section("Invited talks and selected events", [
    ("2025", "Invited talk, Brown Bag Seminar, Arizona State University"),
    ("2025", "Selected lightning talk, CMU Industry-Academia Partnership (IAP) Workshop"),
    ("2025", "Selected participant, Human-AI Teaming for Decision-Making Workshop"),
    ("2024", "Speaker, <i>Turing-like Experiment in a Cyber Defense Game</i>, AAAI Spring Symposium on Human-Like Learning"),
    ("2024", "Speaker, <i>Human-AI Team Defense Game</i>, Women in Cybersecurity (WiCyS)"),
    ("2023", "Invited panelist, <i>Multi-defender collaboration for threat intelligence sharing</i>, The Future of Cyber Deception Workshop"),
    ("2023", "Invited speaker, <i>Using cognitive agents to collaborate with cyber defenders</i>, INFORMS"),
    ("2023", "Speaker, <i>Human-AI Teaming for Cyber Defense</i>, Ellis-DDMLab Workshop"),
    ("2023", "Speaker, <i>Cognitive Modeling of Attackers</i>, Women in Cybersecurity (WiCyS)"),
    ("2022", "Speaker, <i>Learning about attackers through interactive cyber defense games</i>, CyLab Partners Conference"),
    ("2021", "Speaker, <i>Cognitive Modeling of Attackers</i>, CyLab Partners Conference"),
])

s += section("Teaching", [
    ("2025 Fall", "Guest lecture, Graduate Research Methods — how to give an effective presentation"),
    ("2025 Fall", "Guest lecture, Introduction to Artificial Intelligence (undergraduate) — function approximation and deep reinforcement learning"),
    ("2025 Summer", "Teaching assistant, Demystifying AI for Everyone: Concepts and Applications — designed coding-free in-class activities"),
    ("2024 – 2025", "Eberly Future Faculty Program participant — course design, pedagogy seminars, teaching consultations, syllabus design project"),
    ("2024 Spring", "Teaching assistant, 88-312 Decision Models and Games"),
    ("2023 Fall", "Teaching assistant, 17-759/17-599 Advanced Topics in Machine Learning and Game Theory — designed the programming assignment on strategic language agents"),
])

s += section("Other research and industry experience", [
    ("2020", "Independent study, Dynamic Decision Making Lab, Carnegie Mellon University (advisor: Palvi Aggarwal)"),
    ("2020", "Research student, Mobile, Embedded &amp; Wireless Security Lab, Carnegie Mellon University (advisor: Patrick Tague)"),
    ("2020", "Software engineer intern, BlockApps Inc."),
    ("2018", "Research intern, Key Lab for Intelligent Networks and Network Security, Xi'an Jiaotong University (advisor: Jing Tao)"),
])

s += section("References", [
    ("Cleotilde Gonzalez", "Full Research Professor, Carnegie Mellon University"),
    ("Prashanth Rajivan", "Assistant Professor, University of Washington"),
    ("Fei Fang", "Associate Professor, Carnegie Mellon University"),
    ("Palvi Aggarwal", "Assistant Professor, University of Texas at El Paso"),
    ("Christian Lebiere", "Research Scientist, Carnegie Mellon University"),
], w0=1.55)

s.append(Paragraph("Contact details for references available on request. Publications are listed separately. Last updated 2026-08.", note))

doc.build(s)
print("built")
