def add(n):
    result = 0
    for i in range(1,n+1):
        result = result +i
    return result 

def for2(n):
    for i in range (2,n,2):
        print(i)

#print(add(int(input())))
for2(int(input()))

