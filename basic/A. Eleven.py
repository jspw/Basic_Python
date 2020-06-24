def fib(n):
    l=[]
    a=1
    b=1
    l.append(a)
    l.append(b)
    i=0
    while(i<n-2):
        c=a+b
        l.append(c)
        a=b
        b=c
        i=i+1

fib(int(input()))
    