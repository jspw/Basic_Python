def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def revString(n):
    return n[::-1]


while(True):
    try:
        n=input()
    except EOFError:
        break 
    
    if(isPrime(int(n)) == False):
        print("{} is not prime.".format(n))
    else:
            if(n==revString(n)):
                print("{} is prime.".format(n))

            elif(isPrime(int(revString(n)))):
                print("{} is emirp.".format(n))
            else:
                print("{} is prime.".format(n))

