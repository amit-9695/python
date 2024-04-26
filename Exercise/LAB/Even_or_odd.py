def evenodd(a):
    if(a%2==0):
        return 1
    else:
        return -1

a=int(input("Enter a Number :  "))
flag=evenodd(a)
if(flag==1):
    print("Number is Even")
elif(flag==-1):
    print("Number is Odd")
