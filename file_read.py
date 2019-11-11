file = open("test.txt",'r') # 'r' means read 
content = file.read()
print(content)
file.close()

print("New Line")

file = open("test.txt",'r')
content = file.readlines()

print(content)

for line in content[0:10:2]:
    print(line)

file.close()