l=['`','1','2','3','4','5','6','7','8','9','0','-','=','Q','W','E','R','T','Y','U','I','O','P','[',']','A','S','D','F','G','H','J','K','L',';',"'",'Z','X','C','V','B','N','M',',','.','/']
while(True):
    x=[]
    try:
        s=input()

    except EOFError:
        break
    
    for i in s:
        if(i!=' '):
            p=l.index(i)
            x.append(l[p-1])
        else:
            x.append(i)
    
    print(''.join(x))
