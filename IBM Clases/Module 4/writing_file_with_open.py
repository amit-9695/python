#Creating New Text File & Enter the Lines
with open("E:\Text Files\Example 2.txt","w") as File1:
    File1.write("This is Line A \n")
    File1.write("This is Line B \n")

#For Disply the Result
with open("E:\Text Files\Example 2.txt","r") as File1:
    a=File1.read()
    print(a)