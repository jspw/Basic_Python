n,k=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(n-1):
    for j in range(i+1,n):
        #print(l[i]+l[j])
        if((l[i]+l[j])%k==0):
            p+=1
print(p)