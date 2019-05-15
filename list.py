bal = ['apple', 'bal','mal','ele','eaedaaf']
print(bal)

bal.append('ok') #add item to last of the list
print(bal)

print(bal[-1]) # print the last eliment of a list

bal.insert(-1,'shit') #insert element at last position 
print(bal)

del bal[2] #delete element at position 2
print(bal)

x=bal.pop() # remeove last element of list to x 
print(bal)
print (x)

y=bal.pop(1) #remove element at position 1 and insert in y
print(bal)
print(y)

print(bal)
bal.remove("ele") #remove "ele" from item if you know the value of the item
print(bal)

print(bal.index('shit')) #find positon of "Shit" in the list

bal.reverse() # reverse the list
print(bal)

print(bal.reverse()) 

bal.sort() #sort the list alphabetically where Capital letters are 1st order
print(bal) 

bal.sort(reverse = True) # decemebal
print(bal)

print(sorted(bal)) # thie sorted function doeswnt change the list 
print(bal)

x= (sorted(bal))
x.reverse()
print( x)
print(bal)

#list in list

animals = [['cat','mat','rat','bat'],'horse',['dude','bal']]
print(animals) #print list
print(animals[0]) #print first element (list) of list
print(animals[2][1]) #print list of list element at position 1 of 2
print(animals[2][0][1]) #print u know what i mean .....

#list function

x='10000'
bal=list(x)
print(bal)