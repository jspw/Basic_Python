import sys
n=int(input())
fast = "I "
last=" it"
mid=" hate "
i=int(2);
if n==1 :
    print("I hate it")
    sys.exit(0)
else :  
    while 1<i<=n :
     #   print("1")

        if (i%2)==0 :
            mid = mid + " that I love "
        #    print("2")

        else :
            mid = mid + " that I hate "
        #   print("3")

        i=i+1;

print(fast+mid+last)
