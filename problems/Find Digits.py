t=int(input())

for _ in range(t):
    l=[]
    s=input()
    for i in s:
        l.append(i)
        #print(i)
    l=set(l)
    print(len(l))
