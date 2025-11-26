import math as mt
def is_valid(sideA, sideB, sideC):
    return (sideA + sideB) > sideC and (sideB + sideA) > sideA and (sideC + sideA) > sideB

def find_Area(sideA, sideB, sideC):
    s = (sideA+sideB+sideC) / 2
    return mt.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC))

sideA = float(input('Enter length of side A: '))
sideB = float(input('Enter length of side B: '))
sideC = float(input('Enter length of side C: '))

if is_valid(sideA, sideB, sideC):
    print("The area is {:.2f}".format(find_Area(sideA, sideB, sideC)))
else:
    print("invalid")
