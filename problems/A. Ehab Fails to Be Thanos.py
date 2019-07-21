n=int(input())
l=sorted(list(map(int,input().split())))
if l[0]==l[-1]:
    print(-1)
else :
    l.sort()
    print(*l)