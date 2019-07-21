while True:
    try:
        a=int(input())
        p=int(input())
        d=int(input())

    except EOFError:
        break
    
    l1=[]
    while(p):
        l1.append(p%2)
        p=p//2
    print(l1)
    l2=[]
    x=int(a)
    for i in range (1,len(l1)):
        if i==1:
            l2.append(x%d)
        else:
            x=(x*x)%d
            l2.append(x)

    sum=1
    for i in range(1,len(l1)):
        #print(i)
        if l1[i]==1:sum=(sum*l2[i])%d

    print(sum%d)
