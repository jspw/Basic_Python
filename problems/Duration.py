t=int(input())
while(t):
    a,b,c,d=map(int,input().split(" "))
    a=a*60 + b
    b=60*c+d
    print((b-a)//60,(b-a)%60)
    t-=1