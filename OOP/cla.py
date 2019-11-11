class A():
    bal=1000
    def __init__(self,p,q):
        self.p=p
        self.q=q
    
    def area(self):
        return self.p*self.q
    def porishima(self):
        return self.q+self.p

class B(A):
    def __init__(self,p,q,r,l):
        super().__init__(p,q)
        self.r=r
        self.l=l


a1=B(1,2,3,4)
print("The area is : {}".format(a1.area()))
print("The porishima is : {}".format(a1.porishima()))

print(a1.r)
print(a1.p)
print(a1.bal)



        
