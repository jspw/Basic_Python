while(True):
    try:
        n,k=map(int,input().split())
        text=input()
    except EOFError:
        break

    p=0
    for i in range(1,n):
        if text[0:i]==text[n-i:n]:
            p=i
    #print(p)
    s=text+text[p:]*(k-1)
    print(s)