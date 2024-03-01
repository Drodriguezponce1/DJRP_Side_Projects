#intro to files, this works if the file is in the same location
myFile = open("myFile.txt")

#prints out all lines of the text file
print(myFile.read())

#reading the file again means u have to return the buffer to the top
myFile.seek(0)

print(myFile.readlines())
myFile.close()

#gonna read the java text file
#myFile = open("C:\\Users\\Danny\\Documents\\GH_Clone\\DJRP_Side_Projects\\OSRS\BarrowsText.txt")
#print(myFile.readlines())

myFile.close()

#use this instead of closing it!!
with open("myFile.txt") as myFile:
    content = myFile.read()
    print(content)

#write to a file
    # mode = 'r' -> READ ONLY
    # mode = 'w' -> WRITE ONLY (OVERWRITE OR CREATE NEW ONES!)
    # mode = 'a' -> APPEND ONLY (ADD ON TO A FILE)
    # mode = 'r+' -> READ + WRITING ONLY
    # mode = 'w+' -> READING + WRITING ONLY (OVERWRITES EXISTING FILES OR CREATES NEW FILES)
with open(file="newMyFile.txt",mode="w") as myFile:
    myFile.write("This is the first line\nI created this file")

with open(file="newMyFile.txt", mode="a") as f:
    f.write("\nAdding this new line")

with open(file= "newMyFile.txt", mode = "r") as f:
    print(f.readlines())

with open(file="random.txt", mode ="a") as f:
    f.write("Hello")