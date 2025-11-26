import math

number = int(input("Enter a number between 0 and 5000: "))
ishave = False
i = 0
while(True):
    term = ((i)**2 + i) / 2
    if term == number:
        print("{} is a triangular number and it is the {}th number.".format(number, i))
        ishave = True
        break
    if term > number:
        ishave = False
        break
    i += 1
    
if ishave == False:
    print("{} is NOT a triangular number.".format(number))


