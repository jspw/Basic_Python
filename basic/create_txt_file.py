file_name = input("Enter file name : ")
file = open(file_name,'w')
x=input("Enter text : ")
file.write(x)
file.close()
