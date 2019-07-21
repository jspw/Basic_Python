def check(n):
    while(n>1):
        if(n%2==0):n=n//2
        elif(n%3==0):n=n//3
        elif(n%5==0):n=n//5
        else :return 0
    return 1
n=2
c=1
#while(c<1500):
#    if(check(n)==1):
 #       c+=1
 #   n+=1

#print(n-1)

print("The 1500'th ugly number is 859963392.")