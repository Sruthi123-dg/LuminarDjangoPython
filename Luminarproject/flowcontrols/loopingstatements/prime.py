num=int(input("enter the number"))
flag=1
for i in range(2,num):
    if(num%i==0):
        flag=0
        break
if(flag==1):
    print("prime")
else:
    print("not a prime")

