def CountDigit(iNo):
    iCnt=0
    while(iNo>0):
        iCnt=iCnt+1
        iNo=iNo//10
    print("Numer of digit are ",iCnt)    
iNo=int(input("Enter number\n"))
CountDigit(iNo)
