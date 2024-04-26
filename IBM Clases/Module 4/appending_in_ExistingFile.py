#Appending one Line In "Example 1.txt" File by The using mode "a"
with open("E:\Text Files\Example 1.txt","a") as File1:
    File1.write("\nThis is the Third New Appending Line")

#Displaying the Result
with open("E:\Text Files\Example 1.txt","r") as File1:
    a=File1.read()
    print(a)

