'''
User enter integet and outputs whether the number is divisible by both 5 and 6

if (num % 5 == 0) and (num % 6 == 0)
    print output
else
    print output
'''

def Check(number):
    if (number % 5 == 0) and (number % 6 == 0):
        print("{:.0f} is divisible by 5 and 6".format(number))
    else:
        print("{:.0f} is not divisible by 5 and 6".format(number))


number = int(input("Enter an integer number: "))
Check(number)

