#! python3
#Os Module
import os 
print("Welcome ! This is a programme to delete the same files in different directories")

path1=input("Enter path1 : ")
x1 = os.listdir(path1)

path2=input("Entrt path2 : ")
x2 = os.listdir(path2)

for i in x1 : 
    if i in x2 :
        commonFile = os.path.join(path2,i)
        os.remove(commonFile)

print("All Done")