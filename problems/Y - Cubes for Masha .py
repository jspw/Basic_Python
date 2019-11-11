t=int(input())
l=[]
ar=[1,2,3,4,5,6,7,8,9]
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split(" "))
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.append(e)
    l.append(f)
    
l.sort()
print(l)

for i,j in range(1,10):


zero=False
x=-1

if(0 in l):
    zero=True

for i in range(len(l)-1):
    if(l[i]!=0):
        if([i]==l[i+1]):
            i+=1
        else:
            p=l[i-1]
            x=i

if(x==len(l)-1):

