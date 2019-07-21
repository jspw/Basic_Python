from sys import stdin
for n in stdin:
    n=int(n)
    i=1
    while(n):
        l=list(map(int,input().split(" ")))
        print("Case {}: {}".format(i,max(l[1:])))
        i+=1
        n-=1
