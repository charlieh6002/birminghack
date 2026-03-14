import pikepdf

with pikepdf.open("pdf4.pdf") as pdf:
    pdf.save("repaired_pdf.pdf", linearize=True)