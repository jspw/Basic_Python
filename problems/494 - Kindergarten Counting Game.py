while(True):
    
    p=0
    try:
        st=input()

    except EOFError:
        break
    l=0
    for i in st:
        bal=True
        for j in i:
            if (65 <= ord(j) and ord(j) <= 90) or (97 <= ord(j) and ord(j) <= 122):
                if(bal):
                    l+=1
                    bal=False

            else:
                if(bal==False):
                    bal=True

    print(l)


