def sumOfFactor(iNo):
    
    sum=0
    for i in range(1,int(iNo/2)+1):
        if(iNo%i==0):
            sum=sum+i
    
    print("Sum of factor is",sum)        
iNo=int(input("Enter number\n"))
sumOfFactor(iNo)