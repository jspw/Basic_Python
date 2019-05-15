from sys import stdin
def fact(n):
    mul=1
    i=n
    while(i>0):
        mul=mul*i
        i=i-1
    return mul

for x in stdin:
    x=int(x)
    print(str(x)+"!")
    print(fact(x))