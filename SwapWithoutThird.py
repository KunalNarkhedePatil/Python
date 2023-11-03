def swapWithoutThirdNo(iNo1,iNo2):
    iNo1=iNo1+iNo2
    iNo2=iNo1-iNo2
    iNo1=iNo1-iNo2
    print("After swaping:")
    print("Value of iNo1:",iNo1)
    print("Value of iNo2:",iNo2)
iNo1=int(input("Enter first number\n"))    
iNo2=int(input("Enter second number\n"))

print("Befor swaping:")
print("Value of iNo1:",iNo1)
print("Value of iNo2:",iNo2)

swapWithoutThirdNo(iNo1,iNo2)


    
    