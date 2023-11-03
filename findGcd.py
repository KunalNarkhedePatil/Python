def findGcd(iNo1,iNo2):
    i=1
    gcd=0
    while(i<=iNo1 and i<=iNo2):
        if(iNo1%i==0 and iNo2%i==0):
            gcd=i
        i=i+1
    print("Gcd of two number is",gcd)        
            
iNo1=int(input("Enter first number\n"))
iNo2=int(input("Enter second number\n"))

findGcd(iNo1,iNo2)