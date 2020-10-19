num=int(input("enter the number"))
even=0
odd=0
for i in range(1,num):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("even sum=",even)
print("odd sum=",odd)