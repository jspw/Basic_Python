p=int(input("Enter the size of list : "))
l=p
x=[]
while(l):
    x.append(input("Enter elements : "))
    l=l-1

print(x)

while(True) :
    option= int(input("Do you want to :\n1.Pop\n2Remove\n3.Exit\n4.Insert\n5.Append\n6.Search\n7.Sort\n8.Reverse\n9.DecSort ?\n"))


    if(option == 1):
        #POP
        n=int(input("Enter the index you want to pop : "))
        x.pop(n)
        print(x)


    elif(option == 2):
        #Remove
        n=(input("Enter the element you want to remove : "))
        x.remove(n)
        print(x)

    elif(option == 3):
        #Exit
        exit

    elif(option == 4):
        #Insert
        n=int(input("Enter the position : "))
        value = input("Enter the element : ")
        x.insert(n,value)
        print(x)


    elif(option == 5):
        #Append 
        value = input("Enter the element you want to insert : ")
        x.append(value)
        print(x)

    elif (option == 6):
        #search Index
        n=input("Enter the element you want to search ? ")
        if x.index(n) :
            print("Found at " + str(x.index(n)))
        else :
            print("Not Found")
    
    elif (option == 7):
        #Sort
        x.sort()
        print(x)

    elif (option == 8):
        #Reverse
        x.reverse()
        print(x)
    
    elif (option == 9):
        #Decending order
        x=sorted(x)
        x.reverse()
        print(x)


