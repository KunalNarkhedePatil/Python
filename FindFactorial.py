def FindFactorial(iNo):
    iFact=1
    for x in range(1,iNo+1):
        iFact=iFact*x
    return iFact    
        
iNo=int(input("Enter Number\n"))

print("Factorial is ",FindFactorial(iNo))