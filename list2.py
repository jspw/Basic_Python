x=list(range(1,11))
print(x)

for i in x:
    if(i%2==0):
        print(i)

y=[]
for i in x :
    a=i**5
    y.append(a)
print(y)


print(min(x))
print(max(x))
print(sum(x))