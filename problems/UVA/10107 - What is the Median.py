from sys import stdin
l=[]
for i in stdin:
    l.append(int(i))
    l.sort()
    n=len(l)
    #print(l)
    if(n%2==0):
        print((l[n//2] + l[n//2-1])//2)
    else :
        print(l[n//2])