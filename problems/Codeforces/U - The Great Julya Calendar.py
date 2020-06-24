n=input()
p=0
while(int(n)!=0):
    if(len(n)==1):
        p+=1
        break
    l=[int(i) for i in n]
    n=str(int(n)-max(l))
    p+=1
print(p)