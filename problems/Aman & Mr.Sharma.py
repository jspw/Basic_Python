p=0
t=int(input())
for _ in range(t):
    a,b=map(float,input().split(" "))
    a=(2*22*a)
    b=700*b
    if(b>=a):
        p+=1


print(p)