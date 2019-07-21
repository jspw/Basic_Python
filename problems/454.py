n=int(input())
file=open("sample.txt","w")
for i in range(n):
    try:
        if(i==0):
            s1=input()
    except EOFError:
        break
    
    lst=[]
    while True:
        try:
            str=input()
        except EOFError:
            break
        if(str==""):
            break
        lst.append(str)
 #   print(lst)
    lst=sorted(lst)

    for j in range(0,len(lst)):
        for k in range (j,len(lst)):
        # print("IN")
            text=lst[j]
            text=text.replace(" ","")
            text=''.join(sorted(text))
        #    print(text)
            new=lst[k]
            new=new.replace(" ","")
            new=''.join(sorted(new))
        #    print(new)
            if(text==new and j!=k):
            #    output=lst[j]+" = "+lst[k]+"\n"
            #    file.write(output)

                print(lst[j]+" = "+lst[k])
   # file.write("\n")
    if(i!=n-1):
        print()
#file.close()