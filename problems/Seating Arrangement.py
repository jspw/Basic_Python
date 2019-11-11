def oppo(num):
    switcher={
    1: num+11,
    2: num+9,
    3: num+7,
    4: num+5, 
    5: num+3, 
    6: num+1,
    7: num-1,
    8: num-3,
    9: num-5,
    10: num-7,
    11: num-9,
    0: num-11 
    }
    return switcher.get(num%12,"nothing")

test = int(input())
seats=['WS','WS','MS','AS','AS','MS']
for i in range(0,test):
    num= int(input())
    m=num%6
print(oppo(num),seats[m])