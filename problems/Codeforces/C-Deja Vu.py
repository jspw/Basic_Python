def Fibo(n): 
    if n==1: 
        return 1
    elif n==2: 
        return 2
    else: 
        return Fibo(n-1)+Fibo(n-2)

a,b=map(int,input().split())
#print(a,b)
#print(Fibo(a))
print(b%Fibo(a))