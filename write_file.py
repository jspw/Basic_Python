file = open("test.txt",'w')  #'w' will clear the file and rewrite the file

file.write("FUCK OFF")


file.close()

file = open("test.txt",'a') # 'a' will just write dnt delete any data
file.write("OK THEN DONE")