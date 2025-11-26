'''
Generates 2 different numbers

Prompt user to input the total sum of two values generated

if sum is equal to answer then
    print "Your answer is wrong"
else
    print "Your answer is correct"
'''

import random
number1 = random.randint(0,100)
number2 = random.randint(0,100)
answer = number1 + number2
print("-------------------------------------------------------------")
total = "0"

while(str(total) != str(answer)):
    total = input("Enter the sum of {0:d} and {1:d}: ".format(number1, number2))
    if str(total) == str(answer):
        print("Your answer is correct.")

    else:
        print("Your answer is wrong!")

print("-------------------------------------------------------------")

    

