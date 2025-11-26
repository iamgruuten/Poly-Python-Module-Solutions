'''
Prompt user to input weight of parcel in kg
Prompt user if express service is required

IF weight is less than or equal to 1kg THEN
    cost is $10
ELSE IF weight is more than 1kg and less than 5kg THEN
    cost is $15
ELSE IF weight is more than or equal to 5kg THEN
    cost is $20

IF express service is required THEN
    additional cost of $25.50

Output total cost

'''

weight = float(input("Enter weight of parcel in kg : "))
express = input("Is express service required (y/n) : ").upper()

if weight <= 1:
    cost = 10
elif weight < 5:
    cost = 15
else:
    cost = 20
    
if express == "Y":
    cost += 10.50
    
print("The cost is ${:.2f}".format(cost))
