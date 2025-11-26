'''
Input: enter num1 and num2
Process: switch values around
Output: Show the swapped values

'''
#Swapping variables value between 2 inputs

def swap(num1, num2):
    print(f"Your value is {num1} and {num2}")
    num1, num2 = num2, num1
    print(f"Your swapped value is {num1} and {num2} ")

num1 = input("First value: ")
num2 = input("Second value: ")
swap(num1, num2)



