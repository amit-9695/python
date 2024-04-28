# Calculate the BMI
# Formula = weight/(height*height)
# Here Weight will be in kilograms & Hight will be in meter
weight=float(input("Enter The Weight In kg.:- "))
height=float(input("Enter The Height In meter.:- "))
print("The BMI of the person is:-")
print(weight/(height**2))