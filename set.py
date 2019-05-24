#set :-> Unorderes collections of unique elements 
l=[1,2,3,44,54,5,1,2,8,9,10]

x=set()
x.add(1)
x.add(32)
x.add(10)
x.add(1)


print(x)

x.remove(1) # if there is no 1 in set then show error 
x.discard(3) # just delte 3 if there is 3 in set otherwise do nothing
print(len(l))

print(x)
y=x.copy()
x.clear()
print(x)
print(y)

a=set(l)
print(a)

print(len(a))