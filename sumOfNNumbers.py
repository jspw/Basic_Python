def Sum(n):
    sum=0
    i=1
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum

print("Sum of n Numbers = " + str(Sum ( int ( input ("Enter n : ") ) ) ) )