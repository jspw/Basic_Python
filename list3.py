l=[]
for i in range(1,20,2):
    l.append(i)
print(l)

l=[i for i in range(1,100,2**3)]  # list comprehention

print(l)

l= [i**3 for i in range(1,10)] #comprehense
print(l)

bal = [i*2 for i in l]
print(bal)

new = [i for i in bal if i%3==0 and i<=100]
print(new)

list_in_list = [j**2 for j in [i for i in range(1,10) if i%2==0]]
print(list_in_list)


