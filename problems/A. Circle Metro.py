a,b,c,d,e=map(int,input().split(" "))
bl=False
x=a
while(a>0):
 #   print(b,d)
#    print(bl)
    if(b==d):
        bl=True
        break
    
    b+=1
    d-=1
    if(b==d):
        bl=True
        break
    if(b>x):
        b=1
    if(d<1):
        d=x
    if(b==d):
        bl=True
        break
    a-=1

if(bl==False):
    print("NO")
else:
    print("YES")