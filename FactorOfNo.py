def FactorOfNo(iNo):
    num=int(iNo/2)
    for i in range(1,num+1):
        if(iNo%i==0):
            print(i,end=" ")
iNo=int(input("Enter number\n"))
FactorOfNo(iNo)