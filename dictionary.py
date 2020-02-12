bal = {'key1':'Shifat','key2':'Mehedi','key3':'Jannat','key4':'Jyoti'}
bal2= {'key3':'Jannat','key4':'Jyoti','key1':'Shifat','key2':'Mehedi'}

print(bal['key1'])
# This is mapping !
bal['name'] = 'jas'  #insert a value in dictionary
print(bal)

del bal['key2']   # delete a value
print(bal)

del bal2['key2']   # delete a value
print(bal2)

#key method 
print(bal.keys()) #print the keys of  the  dictionary

print (bal.values()) #print values only

for i in bal:  
    print(i)  # will print keys

for i in bal.keys():
    print(i)  # will print keys

for i in bal.values():  
    print(i)  # will print values 
  
# item methods
for i in bal.items():  # print all in a dictionary 
    print(i)

print(bal.items())
print(bal.keys())
print(bal.values())


# item with loops
for i,j in bal.items():
    print(i,j)

del bal['name']

if( bal ==  bal2):
    print("same")
else :
    print ("Not Same")

# in dictionary we can use sorted frunction 
print(sorted(bal.values())) # sprted according to the keys 

for i in sorted(bal.items()):
    print(i)


#new dictionary 

name = {
    1:'Mehedi',
    2:'Hasan',
    3:'Shifat'
 }

for i in name.items():
    print(i)


#nested loop in dictionary
new = [bal,bal2]

for i in new :
    for j,k in i.items():
        print(j,k)


d=dict.fromkeys(['name','age'],'unknown')
print(d)

if (d.get('bal')) :
    print("Have")
print("Ase" if d.get('name') else print("nai"))

x=d.copy()
print(x)

print(x.get('bal',"Not Found"))

print(x.get('unknown',"Not Found"))


