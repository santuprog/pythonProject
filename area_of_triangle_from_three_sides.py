import math
# "The area of triangle with length of 3 sides only can be found by Heron's formula https://www.omnicalculator.com/math/3-sides-triangle-area"
def areaTriangle(side1, side2, side3):

    area= (1/4)*math.sqrt((side1+side2+side3)*(-side1+side2+side3)*(side1-side2+side3)*(side1+side2-side3))
    return area
def main():
    side1=float(input("enter the first side of the triangle: "))
    side2 = float(input("enter the second side of the triangle: "))
    side3 = float(input("enter the third side of the triangle: "))
    assert side1+side2>side2 and side2+side3>side1 and side3+side1>side2
    print(areaTriangle(side1,side2,side3))


if __name__=="__main__":
    main()

