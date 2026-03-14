import os 

def repairHeader(inPath, outPath, fileType):
    #PNG header should be 89 50 4E 47  
    header = b'\x00\x00\x00\x00'
    if fileType == "png" or fileType == "pdf" or fileType == "jpeg" or fileType == "jfif" : 
        if fileType == "png":
            header = b'\x25\x50\x44\x46'
        elif fileType == "pdf":
            header = b'\x89\x50\x4E\x47'
        elif fileType == "jpeg" or fileType == "jfif":
            header = b'\xFF\xD8\xFF\xE0'
    else : 
        raise ValueError("Not a suppported fileType")

    with open(inPath, 'rb') as file: # opens a file called 'file' in the input location and reads it as binary, closes the file immediately after 
        content = file.read() #stores the bytes of the file in content 
    
    if len(content) < 4:
        raise ValueError("File is too small to be a PNG")

    fixedHeader = header + content[4:]

    with open(outPath, 'wb') as file:
        file.write(fixedHeader)

    print("Success!  file saved to: " + outPath)

#need to work out if there is more problems:
repairHeader("cat.png.url", "fixed1.png", "png")
      