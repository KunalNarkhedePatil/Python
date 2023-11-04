def checkPalindrome(iNo):
    rev=0
    Temp=iNo
    while(Temp!=0):
        rev=rev*10+Temp%10
        Temp=Temp//10
    if(rev==iNo):
        print("Number is palindromic")
    else:
        print("Number is not palindromic")    
iNo=int(input("Enter number\n"))
checkPalindrome(iNo)
