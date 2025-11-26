#Programming I

#####################################
#      Mission 3.1                  #
#     Electrical Cost Calculator    #
#####################################

#Background
#==========
#Write a program that prompts user to enter the
#electricity cost for 3 months in a line, separated by ‘;’
#and displays the average electricity cost in 2 decimal places.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - mthly_cost
#   - total
#   - average

#START CODING FROM HERE
#======================
#Prompt for input of electrical costs and store in mthlyCost


#Do not edit the next line
def calculate_average(mthly_cost):
    #Parse the string, extract the electrical cost, and add to the total
    #Hint: Use a combination of the find built-in string method and
    #      index to extract each month's cost, then add it into total
    total = 0
    index = mthly_cost.find(';')
    total = total + float(mthly_cost[0:index])
    
    temp = mthly_cost[index+1:]
    index = temp.find(';')
    total = total + float(temp[0:index])

    temp1 = temp[index+1:]
    total = total + float(temp1)

    average = total / 3
    
    print(average) #Modify to display the average cost

    return average #Do not edit/remove this line

#Do not edit/remove the next line
mthly_cost = input("Input cost value: ")
calculate_average(mthly_cost)

#input '30.5;40.5;20' output 30.333333333333332
#input '25;30;35' output 30.0
