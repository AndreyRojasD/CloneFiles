import shutil
i = 0   
name = '0'
findname = ''
findnamEXT = ''
ext = '.txt'
print("Enter the name of the file to clone")
filetoclone  = input()
print("Enter the number of files to clone")
clonetarget = input()
count = int(clonetarget)
while i <= count:
        number = str(i)
        findname = name + number 
        findnameEXT = findname + ext
        print(findnameEXT)
        i+= 1 
        shutil.copy(filetoclone, findname)