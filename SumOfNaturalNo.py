def sumOfNaturalNo(iNo):
    sum=0
    for i in range(1,iNo+1):
        sum=sum+i
    print("Sum of natural number is",sum)    
iNo=int(input("Enter Number\n"))
sumOfNaturalNo(iNo)