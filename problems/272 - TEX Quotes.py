p=0
while True:
        try :
            st = input()
        except EOFError:
            break

        l=[]
        for i in st:
            if(i =='"'):
                if(p==0):
                    l.append("``")
                    p=1
                else:
                    l.append("''")
                    p=0
            else:
                l.append(i)
                
        print("".join(l))