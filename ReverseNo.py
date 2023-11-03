def reverseNo(iNo):
    rev=0
    while(iNo!=0):
        rev=rev*10+iNo%10
        iNo=iNo//10
    print("Reverse Number is",rev)    
        
iNo=int(input("Enter number\n"))
reverseNo(iNo)