def Main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        p=0
        for i in range(n):
            for j in range(i+1,n):
                if(l[i]>l[j]):
                    l[i],l[j]=l[j],l[i]
                    p+=1

        print("Optimal train swapping takes {} swaps.".format(p))

if __name__ == '__main__':
    Main()