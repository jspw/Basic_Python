import math
def fact(n):
    mul=1
    i=n
    while(i>0):
        mul=mul*i
        i=i-1
    return mul

a,b=(map(int,input().split(" ")))
print(fact(min(a,b)))
