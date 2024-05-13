import math
unit_of_measurement=str(0)

def  getinput():
    unit_of_measurement= str(input("what unit of measurement do you use: "))
    what_utility_input= str(input("""What utility do you want use:  
                                  Enter
                                    1 - for Square
                                    2 - for Rectangle
                                    3 - for pythogoras
                                    4 - for quit
                                    """))
    return what_utility_input

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
    extended_features_input = str(input("Do you want our extended features?"))
    if (extended_features_input=="yes"or"yeah"):
        perimeter_rightangle_triangle = (hypotenuse+width+height)
        area_rightangle_triangle = (width*height)/2
        print("perimeter of your triangle is: ", perimeter_rightangle_triangle, unit_of_measurement)
        print("area of your triangle is: ", area_rightangle_triangle,unit_of_measurement)
    elif (extended_features_input== "no"):
        print("okay")
        what_utility_input = "4"

while True:
    what_utility_input = getinput()
    if (what_utility_input=="1"):
        square()
    if (what_utility_input=="2"):
        rectangle()
    if (what_utility_input=="3"):
        pythogoras()
    if (what_utility_input=="4"):
        break


    
