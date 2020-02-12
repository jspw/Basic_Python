while(True):
    try:
        l=[]
        st=input()
        for i in st:
            l.append(chr(ord(i)-7))
        print(''.join(l))

        

    except EOFError:
        exit