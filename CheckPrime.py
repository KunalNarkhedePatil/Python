def checkPrime(iNo):
    if(iNo==0 or iNo==1):
        return False
    for i in range(2,(int(iNo/2))+1):
        if(iNo%i==0):
            return False
    return True    
iNo=int(input("Enter number\n"))
bRet=checkPrime(iNo)

if(bRet==True):
    print("Number is prime")
else:
    print("Number is not prime")    