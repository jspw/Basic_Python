import os
command=os.system(input("Enter your command : ")) #Exeuting a shell command
print(command)  


#print(os.environ())

current_directory = os.getcwd()  ##Returns the current working directory.

print(current_directory)

#print(os.getgid())

print(os.uname())


path= input("Enter path : ")
#os.chroot(path)  # change directory

os.mkdir(current_directory) # make dircetory 



