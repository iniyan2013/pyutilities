import math
unit_of_measurement= str(input("what unit of measurement do you use: "))
what_utility_input= str(input("what utility do you want use: "))
def rectangle():
    Height = float(input("what is the height: "))
    width = float(input("what is the width: "))
    perimeter = (Height+width)*2
    area = (Height*width)
    print ("perimeter: ",perimeter,unit_of_measurement,"s")
    print ("area: ",area,unit_of_measurement,"s")

def square():
    side = float(input("what is the length of one side:"))
    perimeter_of_square = side*4
    area_of_square = side**2
    print ("perimeter: ",perimeter_of_square,unit_of_measurement)
    print ("area: ",area_of_square,unit_of_measurement)
    
def pythogoras():
    height = float(input("what is the height: "))
    width = float(input("what is the width: "))
    height_square= height**2
    width_square= width**2
    square_of_hypotenuse= height_square+width_square
    hypotenuse = math.sqrt(square_of_hypotenuse)
    print("hypotenuse: ", hypotenuse,unit_of_measurement)
    
    
if (what_utility_input=="square"):
    square()
if (what_utility_input=="rectangle"):
   rectangle()
if (what_utility_input=="pythogoras"):
    pythogoras()
