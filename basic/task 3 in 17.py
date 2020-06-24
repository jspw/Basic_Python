def position2(search,target):
    a=(search.find(target))
    y=(search.find(target,a+1))
    return y


x=input("Enter a string with twin words ")
twin=input("Input the words you want to find ")
print(position2(x,twin),"\nHappy Twin")

   
