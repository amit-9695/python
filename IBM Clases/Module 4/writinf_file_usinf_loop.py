#Creating New Text File & Enter the Lines
Lines=["This is Line 1 \n","This is Line 2 \n","This is Line 3 \n","This is Line 4 \n","This is Line 5 \n"]
with open("E:\Text Files\Example 3.txt","w") as File1:
    for line in Lines:
        File1.write(line)

#For Disply the Result
with open("E:\Text Files\Example 3.txt","r") as File1:
    a=File1.read()
    print(a)