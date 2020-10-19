num=int(input("enter the number"))
sum=0
while(num>0):
    r=num%10
    sum=sum+(r*r*r)
    num=num//10
print(sum)