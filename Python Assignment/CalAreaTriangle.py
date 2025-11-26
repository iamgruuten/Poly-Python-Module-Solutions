'''
Formula = math.sqrt()
user input 3 sides value

'''
import math

def calarea(a,b,c):
    s = (a+b+c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Input lengths can form a triangle of area {:.2f} square units".format(area))
    

sideA = float(input("Enter length of Side A: "))
sideB = float(input("Enter length of Side B: "))
sideC = float(input("Enter length of Side C: "))

if sideA + sideB > sideC and sideB + sideC > sideA and sideA + sideC > sideB:
    calarea(sideA,sideB,sideC)
    
else:
    print("Input lengths cannot form a triangle")
