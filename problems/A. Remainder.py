l,x,y=input().split(' ')
l=int(l)
x=int(x)
y=int(y)
p=0
n=input()
text = list(n[l-x:])
pattern = []

for i in range(x):
    pattern.append('0')
pattern[(x-y-1)]='1'

for i in range (x):
    if(text[i]!=pattern[i]):
        p=p+1
print(p)