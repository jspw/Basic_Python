def Sum(x):
    sum=0
    while(x!=0):
        sum=sum+x%10
        x=x//10
    return sum

print(Sum (int(input())))