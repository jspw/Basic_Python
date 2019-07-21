def product(l):
    pro=1
    for i in l:
        pro=pro*i
    return pro

n=int(input())
l=[]
l=[i for i in range(1,n+1)]
#print("P")
print(product(l))