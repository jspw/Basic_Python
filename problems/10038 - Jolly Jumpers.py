from sys import stdin
l=[]
for l in stdin:

    l=l.split(" ")
    n=int(l[0])
    if(len(l) == 2):
        if('1' in l):
            print("Jolly")
        else :
            print("Not jolly")
    else:
        li=[]
        for i in range(1,len(l)-1,1):
            li.append( abs( int(l[i]) - int(l[i+1]) ) )

        l=set(li)
        #print(l)

        if(1 in l and (n-1) in l):
            if(0 in l and len(l)==n):
                    print("Jolly")
            elif(len(l)==n-1):
                print("Jolly")
            else:
                print("Not jolly")   
        else :
            print("Not jolly")
