import os 
import pikepdf

def repairPDFHeader(inPath, outPath):
    #PDF header should be 25 50 44 46 
    PDFHeader = b'\x25\x50\x44\x46'

    with open(inPath, 'rb') as file: # opens a file called 'file' in the input location and reads it as binary, closes the file immediately after 
        content = file.read() #stores the bytes of the file in content 
    
    #replaces first 4 bytes with the correct pdf ones
    fixedHeader = PDFHeader + content[4:]

    tempFixed = "tempFixed.pdf"
    with open(tempFixed, 'wb') as file:
        file.write(fixedHeader)

    #fix the internal file stuff??
    try:
        with pikepdf.open(tempFixed, allow_overwriting_input = True) as pdf:
            pdf.save(output_path)
        print("Success!  file saved to: " + outPath)
    except Exception as e: 
        print("internal file repair stuff failed" + e)
    finally: 
        if os.path.exists(tempFixed):
            os.remove(tempFixed)

repairPDFHeader()
        
