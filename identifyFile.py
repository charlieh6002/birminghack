def repairHeader(inPath):
    with open(inPath, 'rb') as file: # opens a file called 'file' in the input location and reads it as binary, closes the file immediately after 
        content = file.read() #stores the bytes of the file in content 
    header = content[0:4]
    if header == b'\x89\x50\x4E\x47':
        fileType = "png"
    elif header == b'\x25\x50\x44\x46':
        fileType = "pdf"
    elif header == b'\xFF\xD8\xFF\xE0':
        fileType = "jpeg or jfif"
    return fileType

#main program 
print("The file type is: " + repairHeader("fixed1.png"))

    