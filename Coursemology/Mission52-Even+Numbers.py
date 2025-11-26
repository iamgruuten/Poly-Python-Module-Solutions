#Programming I

########################
#     Mission 5.2      #
#  Loop even integers  #
########################

#Background
#==========
#Write a program that uses while loop to total up the even integers from 1 to 20.


#Important Notes
#===============
#You MUST use the following variables
#   - total
#   - number



#START CODING FROM HERE
#======================

#Set number value
number = range(1,21)


#Check closest object
def total_num(number):
    total = 0
    index = 0
    while index != len(number):
        if (number[index] % 2) == 0:
            total = total + number[index]
            print(total)
        index += 1
            
    print('The total is {}'.format(total)) #Modify to display the total
    
    return total #Do not remove this line

    
#Do not remove the next line
total_num(number)


#output 110
