def mod(num, a): 
      
    # Initialize result 
    res = 0
  
    # One by one process all digits 
    # of 'num' 
    for i in range(0, len(num)): 
        res = (res * 10 + int(num[i])) % a; 
  
    return res

while True:
    try:
        str=input()
    except EOFError :
        break
    bol=True
    p=mod(str,4) 
    q=mod(str,100)
    r=mod(str,400)
    s=mod(str,15)
    t=mod(str,55)

    if((p==0 and q!=0) or r==0):
        print("This is leap year.")
        bol=False
    if(s==0):
        print("This is huluculu festival year.")
        bol=False
    if(((p==0 and q!=0) or r==0) and t==0):
        print("This is bulukulu festival year.")
        bol=False
    if(bol):
        print("This is an ordinary year.")
    print("\n")
