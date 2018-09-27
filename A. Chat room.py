n=int(input())
i=int(1)
while (i<=n):
                s=input()
                h=s.find("h")

                a=s.find("a",h)

                c=s.find("c",a)

                k=s.find("k",c)

                e=s.find("e",k)
                r=s.find("r",e)
                r1=s.find("r",r+1)
                a1=s.find("a",r1)
                n=s.find("n",a1)
                k1=s.find("k",n)

                if(h<a<c<k<e<r<r1<a1<n<k1):
                    print("YES")
                else:
                    print("NO")
                i=i+1
