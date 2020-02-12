from sys import stdin
for x in stdin:

    ch=False
    m=-1

    n,budget,hotel,weekend = x.split(' ')

    n=int(n)
    budget=int(budget)
    hotel = int(hotel)
    weekend = int(weekend)



    for i in range(0,hotel):
    #    print("Enter for hotel  vara : ")
        x=int(input())
    #    print("Enter weened beds : ")
        l=(input().split())
            
        for j in l:
            if(int(j)>=n):
                ch = True
                break

        if(ch):
            m=min(m,n*x)
        #    print(m)
        

    if(m<=budget):
        print(m)
    else :
        print("stay home")
        
