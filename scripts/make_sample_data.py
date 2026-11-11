"""Generate DUMMY import documents for the Claude Code demo session.

All companies, numbers and documents are fictional.
Deliberate discrepancies (for the "find the mismatch" exercise):
  1. Short Rib: invoice price 11.85/kg vs PO 11.50/kg
  2. Beef Tongue: 115 cartons shipped vs 120 ordered
  3. Brisket: invoice net weight 6,512.8 kg vs packing list 6,498.3 kg
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet

OUT = Path(__file__).resolve().parent.parent / "sample-data"
OUT.mkdir(exist_ok=True)
SUPPLIER = "SAMPLE Meat Exports Pty Ltd (fictional)"
BUYER = "SAMPLE Trading Inc. (fictional)"

po_items = [  # code, desc, cartons, kg, usd/kg
    ("CR-01", "Beef Chuck Roll, frozen", 400, 10800.0, 7.20),
    ("SR-02", "Beef Short Rib, frozen", 200, 5000.0, 11.50),
    ("TG-03", "Beef Tongue, frozen", 120, 2400.0, 13.80),
    ("BK-04", "Beef Brisket, frozen", 250, 6500.0, 6.40),
]
inv_items = [
    ("CR-01", "Beef Chuck Roll, frozen", 400, 10812.4, 7.20),
    ("SR-02", "Beef Short Rib, frozen", 200, 4986.0, 11.85),
    ("TG-03", "Beef Tongue, frozen", 115, 2301.5, 13.80),
    ("BK-04", "Beef Brisket, frozen", 250, 6512.8, 6.40),
]
pl_items = [  # code, desc, cartons, net kg, gross kg, prod date, best before
    ("CR-01", "Beef Chuck Roll, frozen", 400, 10812.4, 11292.4, "2026-09-14", "2028-09-13"),
    ("SR-02", "Beef Short Rib, frozen", 200, 4986.0, 5226.0, "2026-09-15", "2028-09-14"),
    ("TG-03", "Beef Tongue, frozen", 115, 2301.5, 2416.5, "2026-09-15", "2028-09-14"),
    ("BK-04", "Beef Brisket, frozen", 250, 6498.3, 6798.3, "2026-09-16", "2028-09-15"),
]

# --- Purchase order (Excel) ---
wb = Workbook()
ws = wb.active
ws.title = "PO-2026-0148"
ws.append(["PURCHASE ORDER  PO-2026-0148   *** SAMPLE / DUMMY DATA ***"])
ws["A1"].font = Font(bold=True)
ws.append(["Buyer", BUYER])
ws.append(["Supplier", SUPPLIER])
ws.append(["Date", "2026-08-20"])
ws.append(["Incoterm", "FOB Brisbane"])
ws.append(["Currency", "USD"])
ws.append([])
ws.append(["Item code", "Description", "Cartons", "Net weight (kg)", "Price (USD/kg)", "Amount (USD)"])
for c in ws[8]:
    c.font = Font(bold=True)
for code, desc, ctn, kg, p in po_items:
    r = ws.max_row + 1
    ws.append([code, desc, ctn, kg, p, f"=D{r}*E{r}"])
last = ws.max_row
ws.append(["TOTAL", "", f"=SUM(C9:C{last})", f"=SUM(D9:D{last})", "", f"=SUM(F9:F{last})"])
for col, w in zip("ABCDEF", (12, 30, 10, 16, 15, 15)):
    ws.column_dimensions[col].width = w
wb.save(OUT / "PO-2026-0148.xlsx")

# --- PDFs ---
styles = getSampleStyleSheet()
def pdf(name, title, meta, header, rows, total_row):
    doc = SimpleDocTemplate(str(OUT / name), pagesize=A4, title=title)
    story = [Paragraph(f"<b>{title}</b>", styles["Title"]),
             Paragraph("<font color='red'>*** SAMPLE / DUMMY DOCUMENT — NOT A REAL TRANSACTION ***</font>", styles["Normal"]),
             Spacer(1, 10)]
    for k, v in meta:
        story.append(Paragraph(f"<b>{k}:</b> {v}", styles["Normal"]))
    story.append(Spacer(1, 12))
    t = Table([header] + rows + [total_row], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
    ]))
    story.append(t)
    doc.build(story)

meta_common = [("Seller", SUPPLIER), ("Buyer", BUYER), ("Buyer PO", "PO-2026-0148"),
               ("Vessel / Voyage", "SAMPLE STAR V.112E"), ("Container", "SMPU 123456-7 (40' Reefer, -18°C)"),
               ("Port of loading", "Brisbane"), ("Incoterm", "FOB Brisbane")]

inv_rows = [[c, d, f"{n}", f"{kg:,.1f}", f"{p:.2f}", f"{kg*p:,.2f}"] for c, d, n, kg, p in inv_items]
pdf("Invoice-INV-88231.pdf", "COMMERCIAL INVOICE  INV-88231",
    [("Invoice date", "2026-10-02")] + meta_common + [("Payment terms", "T/T 30 days after B/L date")],
    ["Code", "Description", "Cartons", "Net kg", "USD/kg", "Amount USD"], inv_rows,
    ["TOTAL", "", f"{sum(i[2] for i in inv_items)}", f"{sum(i[3] for i in inv_items):,.1f}", "",
     f"{sum(i[3]*i[4] for i in inv_items):,.2f}"])

pl_rows = [[c, d, f"{n}", f"{nk:,.1f}", f"{gk:,.1f}", pd, bb] for c, d, n, nk, gk, pd, bb in pl_items]
pdf("PackingList-INV-88231.pdf", "PACKING LIST  (ref. INV-88231)",
    [("Date", "2026-10-02")] + meta_common,
    ["Code", "Description", "Cartons", "Net kg", "Gross kg", "Prod. date", "Best before"], pl_rows,
    ["TOTAL", "", f"{sum(i[2] for i in pl_items)}", f"{sum(i[3] for i in pl_items):,.1f}",
     f"{sum(i[4] for i in pl_items):,.1f}", "", ""])

print("written to", OUT)
