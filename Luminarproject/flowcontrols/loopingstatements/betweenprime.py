low=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
for i in range(low,upper+1):
    flag = 1
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=0
            break
    if(flag==1):
        print(i)
