def rev(s):
    return s[::-1]
t=int(input())
for _ in range(t):
    n=int(input())
    p=0
    while(True):
        n=n+int(rev(str(n)))
        p+=1
        if(str(n)==rev(str(n))):
            break
    print(p,n)
