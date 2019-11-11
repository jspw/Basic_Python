
try:
    x=int(input())
    y=int(input())
    if(x>y):
        print(x)
    else :
        print(y)
except : # if error occurse then except will work
    print("Bokachoda")
else :  # else  will run if no error occur 
    print("All Done")

finally : # finally will work if it has error or not
    print("D")
# cant use finally and else both 
# but can except and finally both 