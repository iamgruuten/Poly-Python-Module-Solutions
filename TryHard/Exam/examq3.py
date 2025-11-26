'''
Prompt user to enter card 1
get value of card 1

Prompt user to enter card 2
get value of card 2

Prompt user to enter card 3
get value of card 3

IF card 1 or card 2 or card 3 is more than 10 THEN
    set its card value to 10
ENDIF

calulcate total value of the hand

IF total value is more than 21 THEN
    ace is counted as 11
    IF card 1 or card 2 or card 3 is equals to 1 THEN
        set its card value to 11

ELSE
    ace is counted as 1
    IF card 1 or card 2 or card 3 is equals to 1 THEN
        set its card value to 1
ENDIF
calculate total values again
Display total value
'''

card1 = int(input("Enter card 1: "))
card2 = int(input("Enter card 2: "))
card3 = int(input("Enter card 3: "))

if card1 > 10:
    card1 = 10
    
if card2 > 10:
    card2 = 10
    
if card3 > 10:
    card3 = 10

total = card1 + card2 + card3

print("Total value is {}".format(total))
