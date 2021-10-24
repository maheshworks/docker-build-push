import os
f = open("FirstFile.txt","w")
f.write("This is for testing")
f.close()
#f = open("FirstFile.txt","r")
#print(f.read())
#if os.path.exists("FirstFile2.txt"):
#    os.remove("FirstFile2.txt")
#    os.rmdir("myfolder")
#else:
#    print("File doesn't exist")

x = open("FirstFile.txt", "r")

print(x.readlines())
print(x.seek(1))
with open("FirstFile.txt", "a") as file1:
    file1.write("Welcome to with statement")
    
with open("FirstFile.txt", "r") as file1:
    print(file1.read())
