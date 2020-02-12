l=int(input())
t=int(input())
while(t):
    a,b=map(int,input().split(" "))
    print( "UPLOAD ANOTHER" if(a<l or b<l) else ( "ACCEPTED"if a==b  else "CROP IT"))
    t-=1