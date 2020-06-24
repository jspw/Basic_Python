t=1
while(True):
    x=input()
    if(x=='*'):
        break;
    
    elif(x=='Hajj'):
        print("Case {}: Hajj-e-Akbar".format(t))
    else :
        print("Case {}: Hajj-e-Asghar".format(t))
    t+=1
