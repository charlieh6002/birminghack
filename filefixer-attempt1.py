import pikepdf
import os

broken_file = "pdf2.pdf"
os.remove("repaired_pdf.pdf")
new_file = open("repaired_pdf.pdf", "x")
new_file.close()

def repair_pdf(input_path, output_path):
    try:
        with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
            pdf.save(output_path)
        #print("Repaired PDF saved to:", output_path)
    except Exception as e:
        print("Repair failed:", e)

repair_pdf(broken_file, "repaired_pdf.pdf")
