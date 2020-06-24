def evenSum(a):
    a=a//2
    return a*(a+1)

def oddSum(a):
    if(a%2==0):
        a=a//2
    else:
        a=a//2+1
    #print(a)
    return a*a

t=int(input())
i=1
while(i<=t):

    r,l=(input().split(" "))
    r=int(r)
    l=int(l)
    if(r==l):
            if(r%2==0):
                print(r)
            else :
                print(-r)

    else :
        rSum = evenSum(r) - oddSum(r)
        lSum= evenSum(l) - oddSum(l)
        if(r%2==0):
            print(rSum-lSum+r)
        else:
            print(rSum-lSum-r)
         
    i=i+1