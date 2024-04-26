# Asking for Input from the user
height=float(input("Enter the Height in cm.:- "))
weight=float(input("Enter the weight in kg.:- "))
BMI=weight/(height/100)**2
print("\nyour Body Mass Index(BMI) is= ",BMI)
if BMI<=18.5:
    print("Oops! You are underweight.")
elif BMI<=24.9:
    print("Awesome! You are healthy.")
elif BMI<=29.9:
    print("Eee! You are over Weight.")
else:
    print("Seesh! You are obese.")


