# in Python there are two types of membership operator-- in and notin
#Lets take a example of string
str= "Amit"
print("A" in str)             #True
print("a" in str)             #False
print("A" in "Amit")          #True
print("t" in str)             #True
print("T" in str)             #False
print("s" in str)             #False
print("S" in "Shukla")        #True

print("\n \n")

#Lets take a example of list
l=[1,10,-1,0,17]
print(10 in l)                #True
print(10 not in l)            #False
print(20 in l)                #False
print(20 not in l)            #True