while(True):
    try:
        n=input()
        
    except EOFError:
        break
    l=list((input().split()))
    m=input()
    q=list((input().split()))
    new=[]
    for i in range(min(len(l),len(q))):
        if(l[i]==q[i]):
            new.append(str(i+1))
    print(" ".join(new))