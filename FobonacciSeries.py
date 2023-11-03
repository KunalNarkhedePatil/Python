def fobonacciSeries(a,b,iNo):
    if(iNo==0):
        return
    c=a+b
    print(c,end=" ")
    iNo=iNo-1
    fobonacciSeries(b,c,iNo)
    
iNo=int(input("Enter the number of term\n"))
a=0
b=1
print(a,b,end=" ")
fobonacciSeries(a,b,iNo)