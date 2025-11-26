import math
radius = float(input("Input radius: "))
height = float(input("Input Height: "))
totalsa = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)
print(f"total surface area: {str(totalsa)}cm")
