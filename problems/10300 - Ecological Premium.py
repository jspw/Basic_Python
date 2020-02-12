t=int(input())
while(t):
    sum=0
    n=int(input())
    while(n):
        a,b,c=map(int,input().split(" "))
        sum=sum+a*c

        n-=1
    print(sum)

    t-=1
