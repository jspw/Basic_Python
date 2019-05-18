import os
path = input("Enter the path you wnat to delete : ")
os.rmdir(path) # will delete empty path only
os.remove(path) # will delete files only 
dir = os.getcwd()  #will get the current working directory 
os.chdir(r"C:\Users") # will change current directory
