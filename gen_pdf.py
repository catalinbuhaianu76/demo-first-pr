#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fpdf import FPDF

RED = (200, 16, 46)
GREY = (136, 136, 136)
LIGHT = (245, 245, 245)
DARK = (26, 26, 26)

class Offer(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-18)
        self.set_draw_color(221, 221, 221)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(2)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 6, "Document generat la 08.06.2026  -  Oferta comerciala cu titlu informativ",
                  align="C")

pdf = Offer(format="A4")
pdf.set_auto_page_break(auto=True, margin=20)
pdf.set_margins(20, 18, 20)
pdf.add_page()
W = pdf.w - pdf.l_margin - pdf.r_margin

# ---- Header ----
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(*RED)
pdf.cell(0, 12, "OFERTA COMERCIALA", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*GREY)
pdf.cell(0, 6, "[Numele firmei emitente]   |   CUI: [______]   |   Reg. Com.: [______]",
         new_x="LMARGIN", new_y="NEXT")
pdf.ln(1)
y = pdf.get_y()
pdf.set_draw_color(*RED); pdf.set_line_width(0.8)
pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
pdf.set_line_width(0.2)
pdf.ln(6)

# ---- Meta ----
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*DARK)
def meta_row(l1, v1, l2, v2):
    pdf.set_text_color(*GREY); pdf.cell(28, 6, l1)
    pdf.set_text_color(*DARK); pdf.cell(60, 6, v1)
    pdf.set_text_color(*GREY); pdf.cell(28, 6, l2)
    pdf.set_text_color(*DARK); pdf.cell(0, 6, v2, new_x="LMARGIN", new_y="NEXT")
meta_row("Nr. oferta:", "[___] / 08.06.2026", "Valabilitate:", "60 de zile de la emitere")
meta_row("Data:", "08.06.2026", "Moneda:", "RON (lei)")
pdf.ln(4)

# ---- Recipient ----
y0 = pdf.get_y()
pdf.set_fill_color(*LIGHT)
pdf.rect(pdf.l_margin, y0, W, 16, "F")
pdf.set_fill_color(*RED)
pdf.rect(pdf.l_margin, y0, 1.5, 16, "F")
pdf.set_xy(pdf.l_margin + 5, y0 + 2.5)
pdf.set_font("Helvetica", "", 8)
pdf.set_text_color(*GREY)
pdf.cell(0, 5, "IN ATENTIA", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(pdf.l_margin + 5)
pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(*DARK)
pdf.cell(0, 7, "S.C. FERRERO ROMANIA S.R.L.", new_x="LMARGIN", new_y="NEXT")
pdf.set_y(y0 + 16)
pdf.ln(6)

# ---- Intro ----
pdf.set_font("Helvetica", "B", 10.5)
pdf.cell(0, 6, "Stimata Doamna / Stimate Domnule,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1)
pdf.set_font("Helvetica", "", 10.5)
pdf.multi_cell(0, 6, "Va multumim pentru interesul acordat produselor noastre. Ca urmare a "
    "solicitarii Dumneavoastra, avem placerea de a va transmite urmatoarea oferta comerciala:")
pdf.ln(4)

# ---- Items table ----
headers = ["Denumire produs / serviciu", "Cant.", "Pret unitar\n(fara TVA)",
           "Valoare\n(fara TVA)", "TVA 19%", "Valoare\n(cu TVA)"]
widths = [62, 16, 27, 27, 19, 19]  # sum = 170 = W
aligns = ["L", "C", "R", "R", "R", "R"]

pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(255, 255, 255)
hy = pdf.get_y()
HH = 10  # full header height
# solid red background for the whole header row
pdf.set_fill_color(*RED)
pdf.rect(pdf.l_margin, hy, W, HH, "F")
for w, h, a in zip(widths, headers, aligns):
    x = pdf.get_x()
    lines = h.count("\n") + 1
    # vertically center the text block within the header height
    y = hy + (HH - lines * 5) / 2
    pdf.set_xy(x, y)
    pdf.multi_cell(w, 5, h, border=0, align=a, fill=False, max_line_height=5,
                   new_x="RIGHT", new_y="TOP")
    pdf.set_xy(x + w, hy)
pdf.set_xy(pdf.l_margin, hy + HH)

rows = [
    ["Display TICTAC TWO P144", "20 buc", "77,00", "1.540,00", "292,60", "1.832,60"],
    ["Transport (box)", "20 buc", "7,48", "149,60", "28,42", "178,02"],
]
pdf.set_font("Helvetica", "", 9.5)
pdf.set_text_color(*DARK)
fill = False
for row in rows:
    pdf.set_fill_color(250, 250, 250) if fill else pdf.set_fill_color(255, 255, 255)
    for w, val, a in zip(widths, row, aligns):
        txt = val if (a == "L" or a == "C") else (val + " lei" if val else "")
        pdf.cell(w, 9, txt, border="B", align=a, fill=True)
    pdf.ln(9)
    fill = not fill
pdf.ln(6)

# ---- Totals ----
half = W / 2
pdf.set_x(pdf.l_margin + half)
pdf.set_font("Helvetica", "", 10.5)
pdf.cell(half * 0.6, 7, "Valoare totala fara TVA:", align="L")
pdf.cell(half * 0.4, 7, "1.689,60 lei", align="R", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(pdf.l_margin + half)
pdf.cell(half * 0.6, 7, "TVA (19%):", align="L")
pdf.cell(half * 0.4, 7, "321,02 lei", align="R", new_x="LMARGIN", new_y="NEXT")
gy = pdf.get_y()
pdf.set_fill_color(*RED)
pdf.rect(pdf.l_margin + half, gy, half, 10, "F")
pdf.set_xy(pdf.l_margin + half, gy)
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 12)
pdf.cell(half * 0.55, 10, "  TOTAL DE PLATA:", align="L")
pdf.cell(half * 0.45, 10, "2.010,62 lei  ", align="R", new_x="LMARGIN", new_y="NEXT")
pdf.set_text_color(*DARK)
pdf.ln(8)

# ---- Note ----
pdf.set_font("Helvetica", "", 9.5)
pdf.set_text_color(85, 85, 85)
pdf.multi_cell(0, 5.5, "Preturile sunt exprimate in lei (RON). Oferta este valabila 60 de "
    "zile de la data transmiterii. Ramanem la dispozitia Dumneavoastra pentru orice "
    "informatii suplimentare si va multumim pentru colaborare.")
pdf.ln(10)

# ---- Signature ----
pdf.set_text_color(*DARK)
pdf.set_font("Helvetica", "", 10.5)
pdf.cell(0, 6, "Cu stima,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)
pdf.set_text_color(*GREY)
pdf.cell(0, 6, "_______________________________", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, "[Nume Prenume]", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, "[Functia]", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, "[Firma]  |  Tel: [______]  |  Email: [______]", new_x="LMARGIN", new_y="NEXT")

pdf.output("/home/user/demo-first-pr/Oferta_Ferrero_Romania.pdf")
print("PDF generat cu succes")
