t=int(input())
while(t):
    a,b=map(str,input().split(" "))
    l=[i for i in a]
    k=[i for i in b]
    l.sort()
    k.sort()
    l=''.join(l)
    k=''.join(k)

    print("YES" if l==k else "NO")
    t-=1