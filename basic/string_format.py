x=int(input("Enter x : "))
y=int(input("Enter y : "))

print("The sum is : {}".format(x+y))

print("The sum in float : {0:f}".format(x+y))

print("The ans is  \nx+y = {}\nx-y =  {}\nx*y =  {}\nx/y =  {}\nx//y =  {}".format(x+y,x-y,x*y,x/y,x//y))

print("The ans is  \nx+y = {0}\nx-y =  {1}\nx*y =  {2}\nx/y =  {3}\nx//y =  {4}".format(x+y,x-y,x*y,x/y,x//y))

print("The ans is  \nx+y = {3}\nx-y =  {1}\nx*y =  {0}\nx/y =  {2}\nx//y =  {4}".format(x+y,x-y,x*y,x/y,x//y))

print("The sum is : {0:3d}".format(x+y)) # d is for giving space

print("The sum is : {0:f}".format(x+y))

print("The sum is : {0:.2f}".format(x+y))

print("The sum is : {0:>10}".format(x+y))

print("The sum is : {0:3<}".format(x+y))

print("The sum is : {0:*^5}".format(x+y))

for i in range(1,11,1):
    print("{} {} {}".format(i,i**2,i**3))
