import os
file = open("test.txt",'w') # 'r' means read 
while(True):
    l=input()
    p=0
    c=0
    bol=False
    if(l == '0 0'):
        break

    a,b=l.split(' ')
    a=''.join(reversed(a))
    b=''.join(reversed(b))

    for i in range(min(len(a),len(b))):
        if(int(a[i]) + int(b[i]) + c > 9):
            p+=1
            c=1
        else:
            c=0

    if(len(a)>len(b)):
        for i in range(len(b),len(a)):
            if(int(a[i]) + c >9):
                c=1
                p+=1
            else:
                break
    elif(len(b)>len(a)):
        for i in range(len(a),len(b)):
            if(int(b[i]) + c >9):
                c=1
                p+=1
            else:
                break

    if(p==0):
        #file.write(("No carry operation.\n"))
        print(("No carry operation."))
    elif(p==1):
        #file.write(("{} carry operation.\n".format(p)))
        print(("{} carry operation.".format(p)))
    else:
        #file.write(("{} carry operations.\n".format(p)))
        print((("{} carry operations.".format(p))))
        