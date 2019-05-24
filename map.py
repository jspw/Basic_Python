def negative(n):
    return n*-1

num= [1,2,3,4,5,6,7,8,9]

print(list(map(negative,num)))

print(list(map(lambda a: a**2,num)))

