'''
prompt user to enter total weight of baggage in kg
IF weight is more than 30 kg THEN
    charged amount is excess weight multiple by 12
    print the amount the user has to pay
ELSE
    print the user do not have to pay


'''

weight = float(input("Total weight of baggage (kg) : "))
if weight > 30:
    excess = weight - 30
    amount = excess * 12
    print("Your baggage is {}kg more than the limit of 30kg".format(excess))
    print("You will have to pay ${:.2f}".format(amount))
else:
    print("You do not have to pay for your baggage")
    
