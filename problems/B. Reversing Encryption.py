def string_rev(s):
    return s[::-1]

n=int(input())
text=input()
if(n==1):
    print(text)
else:
    l=[]
    for j in range(1,n//2+1):
            if(n%j==0):
                if(n//j==j):
                    l.append(j)
                else:
                    l.append(j)
                    l.append(n//j)
    l=set(l)
    l=list(l)
    l.sort()
    for i in range(1,len(l)):
        text = string_rev(text[0:int(l[i])]) + text[int(l[i]):]
    
    print(text)


