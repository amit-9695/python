def Areaofrectangle(width, height):
    Area = width * height
    Perimeter = 2 * (width + height)
    print("\n Area of a rectangle is (w * h): %.2f" %Area)
    print("\n Perimeter of rectangle is (2 * (w + h)): %.2f" %Perimeter)
width = float(input('Enter the width of a rectangle: '))
height = float(input('Enter the height of a rectangle: '))
Areaofrectangle(width, height)