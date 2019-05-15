x=int(input())
y=int(input())
i=int(1)
fact=int(1)
while i<=x :
    fact=((fact%y)*(i%y))%y
    i=i+1

print(fact)