import math
while(True):
    n=int(input())
    if(n==0) : break
    print((math.sqrt(n)))
    print("yes" if int(math.sqrt(n))**2 == n else "no")
