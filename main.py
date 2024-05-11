
what_utility_input= str(input("what utility do you want use"))
def rectangle():
    Height = float(input("what is the height "))
    width = float(input("what is the width "))
    perimeter = (Height+width)*2
    area = (Height*width)
    print (perimeter)
    print (area)

def square():
    side = float(input("what is the length of one side"))
    perimeter_of_square = side*4
    area_of_square = side**2
    print (perimeter_of_square)
    print (area_of_square)
if (what_utility_input=="square"):
    square()
if (what_utility_input=="rectangle"):
   rectangle()
