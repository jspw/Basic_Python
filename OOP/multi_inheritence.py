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


class C(B):
    def __init_(self,p,q,r,l,s):
        super().__init__(p,q,r,l)
        self.s=s


a1 = C(3,1,2,2,4)

print("The area is : {}".format(a1.area()))
print("The porishima is : {}".format(a1.porishima()))

print("here r = {}".format(a1.r))
print("Here p = {}".format(a1.p))
print("Here al = {}".format(a1.bal))
print("Here p+q = {}".format(a1.p+a1.q))
print(a1.s)



        
