def findLcm(iNo1,iNo2):
    greter=0
    if(iNo1>iNo2):
        greter=iNo1
    else:
        greter=iNo2
    while(1):
        if(greter%iNo1==0 and greter%iNo2==0):
            break
        greter=greter+1
    print("Lcm of two number is",greter)    
iNo1=int(input("Enter first number\n"))
iNo2=int(input("Enter second number\n"))

findLcm(iNo1,iNo2)