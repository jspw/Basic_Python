l=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
x=[]
n=int(input())
for i in range(1,n+1):
    if i in l:
        x.append('O')
    else:
        x.append('o')
print(''.join(x))