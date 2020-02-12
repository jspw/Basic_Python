def h(n):
    res=0
    for i in range(2,n//2+1):
        res=res+n//i
    return res+n+(n-n//2)

t=int(input())
while(t):
    n=int(input())
    print(h(n))

    t-=1