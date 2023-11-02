def sumOfDigit(iNo):
    sum=0
    while(iNo!=0):
        sum=sum+iNo%10
        iNo=iNo//10
    print("Sum is",sum)    
iNo=int(input("Enter number\n"))
sumOfDigit(iNo)