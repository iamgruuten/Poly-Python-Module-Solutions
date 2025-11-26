'''
input: height, weight
process : weight / (height * height)
output: show bmi
'''

#Calculate BMI

def calculation(height, weight):
    total = weight / (height * height)
    
    print(f"Your Height is {height}m")
    print(f"Your Weight is {weight}kg")
    print(f"Your BMI is {str(total)}")

    return total

def health(bmivalues):
    if bmi > 27:
        print("You are overweight")
    elif bmi < 18:
        print("You are underweight")
    else:
        print("You are healthy")

        
height = float(input("Enter Your Height in m: "))
weight = float(input("Enter Your Weight in kg: "))
bmi = calculation(height, weight)
health(bmi)
