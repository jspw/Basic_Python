def check(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if(l[i]+l[j]==k and i!=j):
                return True
    return False

while(True):
    try:
        t=int(input())
    except EOFError:
        break
    for _ in range(t):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        l.sort()
        print("Yes" if check(l) else "No")