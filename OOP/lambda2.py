def bigger(a,b):
    if(a>b):
        return a
    return b

biggerL = lambda a,b : a if a>b else b

print(bigger (1,2))


first_item = lambda l:l[0]

l=[1,2,3,4]

print(first_item(l))
