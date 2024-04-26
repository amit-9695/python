num=int(input("Enter a Number :- "))

if num<0:
    print("Enter a Position Number :- ")

else:
     sum=0

     while(num>0):
       sum+=num
       num-=1

print("The sum is = ",sum)