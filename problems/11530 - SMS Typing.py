l=['d','g','j','m','p','t','w',' ','a'] #1
m=['e','h','k','n','q','u','x','b'] #2
n=['c','f','i','l','o','r','v','y'] #=3
o=['s','z'] #4

t=int(input())
j=0
while(t):
    j+=1
    s=input();
    p=0
    for i in s:
        if(i in l):
            p+=1
        elif(i in m):
            p+=2
        elif(i in n):
            p+=3
        else:
            p+=4
    print("Case #{}: {}".format(j,p))

    t-=1

