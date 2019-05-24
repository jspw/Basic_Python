import math

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

t=int(input())
while(t>0):
    n=int(input())
    a=input().split(" ")
    q=int(input())
    while(q>0):
        l,r=input().split(" ")
        l=int(l)
        r=int(r)
        s=[]
        if(l==r):
            print(0)
        else :
            for i in range(l-1,r):
                s.append(int(a[i]))
            g  = gcd(max(s),min(s))
            print(g)
        s.clear()
        q-=1

    t-=1