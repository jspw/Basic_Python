name = "Jannat Jyoti Jasmin Jasica Jui JackQ Joya Jyoti"
print(name.find("Jyoti"))  #find a string in a string
l=name.find("Jyoti")
print(name.find("Jyoti",l+1))   #find a string starting from a index
print( name.find("Jyoti",name.find("Jyoti") + 1) )  #find a string starting from a index in a line 
print("HELE")
name = "Jannatul Ferdaous Jyoti"
print("Length of the name : " + str(len(name)))
print(name.find('J'))
if((name.find('Jannat',name.find('J')+1)) != -1):
    print("FOUND")
else :
    print("Not Found")


