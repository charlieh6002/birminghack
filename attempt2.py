import pikepdf
import os

#function to check if a pdf is still corrupted by checking if it can be opened
#this doesn't work for repair_pdf functtion as it creates a uncorrupted blank pdf anyway
def corruptionChecker(pdf_name):
    try:
        with pikepdf.open(pdf_name) as test:
            return True
    except pikepdf.PdfError:
             return False
    

broken_file = "pdf4.pdf"
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

if(corruptionChecker("repaired_pdf.pdf") == True):
     print("fixed??")