while(True):
        try:
            a,b=map(int,input().split(":"))
            
            c,d=map(int,input().split(":"))
        except EOFError:
            break

        x=a*60+b
        y=c*60+d
        br=(y-x)//2
       # print(x,y,br)
        h=a+br//60
        m=b+br%60
        if(m>=60):
            m=m%60
            h+=1
        if(len(str(h))==2 and len(str(m))==2):
            print("{}:{}".format(h,m))
        else:
            if(len(str(h))==1 and len(str(m))==2):
                print("0{}:{}".format(h,m))
            elif(len(str(m))==1 and len(str(h))==2):
                print("{}:0{}".format(h,m))
            else:
                print("0{}:0{}".format(h,m))
