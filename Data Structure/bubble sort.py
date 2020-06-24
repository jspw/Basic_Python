x = int(input())
l=input().split()
# Sort in accending order
for i in range(0,x):
    for j in range(0,x):
        if(l[i]<l[j]):
            l[i],l[j]=l[j],l[i]

for i in l :
    print(i,end = " ")
