while(True):
    try:
        n=input()
    except EOFError:
        break

    l=list((input().split()))
    m=input()
    q=list((input().split()))
    new=[]
    for i in l:
        if(i in q):
            new.append(i)
    new.sort()   
    print(" ".join(new))

