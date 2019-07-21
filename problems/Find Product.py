def product(l):
    pro=1
    for i in l:
        pro=pro*i
    return pro

n=input()
l=list(map(int,input().split(" ")))
#print("P")
print(product(l)%1000000007)