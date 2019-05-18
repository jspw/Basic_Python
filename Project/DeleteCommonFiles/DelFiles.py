#! python3
#Os Module
import os 
print("Welcome !\n\n\nThis is a programme to delete the same files in different directories -_- \n\n")

print(r"NOTE :  I can't delete any folder ! I don't have that permission :) ")

path1=input("\n\nEnter path of the 1st Folder : ")
x1 = os.listdir(path1)

path2=input("\n\nEnter path of the 2st Folder : ")
x2 = os.listdir(path2)

for i in x1 : 
    if i in x2 :
        commonFile = os.path.join(path2,i)
        os.remove(commonFile)

print("All Done")