def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    i=0
    while(i<n-2):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1

fib(int(input()))
    