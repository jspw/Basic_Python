s=input()
print(''.join([i.upper() if(i.islower()) else i.lower() for i in s ]))