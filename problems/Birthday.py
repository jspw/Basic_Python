_ = input()
m = map(int, input().split())
m = sorted(m)
#print(m)

l=[]
for i in range(len(m)):
    if(i%2==0):
        l.append(str(m[i]))

for i in range(len(m)-1,0,-1):
    if(i%2!=0):
        l.append(str(m[i]))

print(' '.join(l))