with open("E:\Text Files\Example 1.txt","r") as File1:
    a=File1.readline()
    print(a)
    #It will Print Only One Line Of The Text File "Example 1.txt"
    #We can Print More Than One Line Of the Text File "Example 1.txt" by reapting the readline method or using the loop

    #Reapeating the readline element
    a = File1.readline()
    print(a)
    #It will print The next one line of the text File

    #Using Loop
    for line in File1:
        print(line)
        #It will print all The reameaning Lines of the text File