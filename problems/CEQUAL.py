t=int(input())
for _ in range(t):
    n=int(input())
    l=set(map(int,input().split()))
    #print(l)
    if(len(l)!=n):
        print("Yes")
    else:
        print("No")
