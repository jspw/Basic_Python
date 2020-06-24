t=int(input())

while(t>0):
    b=False
    l=int(input())
    n=input()
    if(l<11):
        print("NO")
    else :
        n=n[0:l-10]
    #    print(n)
        for i in n:
        #    print(i)
            if(i=='8'):
                b=True
                break

        if(b):
            print("YES")
        else :
            print("NO")
    t=t-1

