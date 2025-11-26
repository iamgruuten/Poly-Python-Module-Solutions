#Programming I

##########################################
#              Mission 5.1               #
#   ERP Rates at Orchard Cordon gantry   #
##########################################

#Background
#==========
#Any cars entering Orchard Road from Scotts Road from Monday to Friday will
#have to pay the following ERP charges depending on the time of entry.





#Write a Python program to check how much the ERP rate is and to deduct this
#amount from the cash card and display its new value.

#The program is to prompt user for the current value in the cash card and the
#time of entry into Orchard Road,and display the ERP rate that has to be paid
#and the new value in the cash card.
#The program will also check if there is enough balance in the cash card to pay
#for the ERP charge.  If not it will display a insufficient balance message.
#
#The return value of the function is a list with two elements:
#   - Final card value
#   - True if deduction is successful, false otherwise


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - time_of_entry
#   - card_value
#   - erp_rate
#   - successful_deduction



#START CODING FROM HERE
#======================

#Prompt user for the current value in the cash card and the
#time of entry into Orchard Road

########################################
#      Time               #  ERP Rate  #
########################################
#  Before 12.00           #    Free    #
#  12.00 <= time < 17.30  #    0.50    #
#  17.30 <= time < 17.35  #    1.00    #
#  17.35 <= time < 18.00  #    1.50    #
#  18.00 <= time < 18.55  #    2.00    #    
#  18.55 <= time < 19.00  #    1.50    #
#  19.00 <= time < 19.55  #    1.00    #
#  19.55 <= time < 20.00  #    0.50    #
#  20.00 or after         #    Free    #
########################################



#Calculate New Value in Cash Card
def calculate_card_value(card_value, time_of_entry):

    #Check ERP rate using if/elif/else
        
        
    print("{0:#<40}".format("")) #Modify to display ERP Rate
    print("{0:}{1:>10}{2:>9}{3:^10}{4:>0}".format("#", "Time", "#", "ERP Rate", "#"))
    print("{0:#<40}".format("")) #Modify to display ERP Rate
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "Before 12.00", "#", "Free", "#"))
    print("{0:}{1:<15}{2:>4}{3:^10}{4:>0}".format("#", "12.00 <= time < 17.30", "#", "0.50", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "17.30 <= time < 17.35", "#", "1.00", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "17.35 <= time < 18.00", "#", "1.50", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "18.00 <= time < 18.55", "#", "2.00", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "18.55 <= time < 19.00", "#", "1.50", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "19.00 <= time < 19.55", "#", "1.00", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "19.55 <= time < 20.00", "#", "0.50", "#"))
    print("{0:}{1:>15}{2:>4}{3:^10}{4:>0}".format("#", "20.00 or after", "#", "Free", "#"))
    print("{0:#<40}".format("")) #Modify to display ERP Rate

    if 20.00 >= time_of_entry <= 12.00 :
        erp_rate = 0
    elif 12.00 <= time_of_entry < 17.30:
        erp_rate = 0.50
    elif 17.30 <= time_of_entry < 17.35:
        erp_rate = 1.00
    elif 17.35 <= time_of_entry < 18.00:
        erp_rate = 1.50
    elif 18.00 <= time_of_entry < 18.55:
        erp_rate = 2.00
    elif 18.55 <= time_of_entry < 19.00:
        erp_rate = 1.50
    elif 19.00 <= time_of_entry < 19.55:
        erp_rate = 1.00
    elif 19.55 <= time_of_entry < 20.00:
        erp_rate = 0.50

    if card_value > erp_rate:  #Check if there is enough balance to pay ERP charge
        card_value = card_value - erp_rate  #Modify to calculate new value in cash card
        print(card_value) #Modify to display new value in cash card
        successful_deduction = True
    else:
        print("insufficient balance in cash card") #Modify to display insufficent balance in cash card
        successful_deduction = false
    return [card_value,successful_deduction] #Do not remove this line

    
#Do not remove the next line

calculate_card_value(card_value, time_of_entry) 

#input 50,18.30 output [48.00, True]
#input 30,20.00 output [30.00, True]
#input 0.50,17.32 output [0.50, False]

