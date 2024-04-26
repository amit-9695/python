def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
add=a+b

#Using F String
print(f'Sum of {a} and {b} is {sum(a, b)}')

#Using .format
print("Sum of {0} and {1} is {2}".format(a,b,add))


print("sum of %d and %d is %d"%(a,b,add))