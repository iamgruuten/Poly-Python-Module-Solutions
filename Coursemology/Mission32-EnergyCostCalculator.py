#Programming I

#######################################
#            Mission 3.2              #
#   Calculate Daily Total Energy Cost #
#######################################

#Background
#==========
#The total energy cost is calculated using this formula: 
#Total Energy Cost ($) = Total Energy consumed (kW) x 0.2356

#Write a Python program that displays a table of energy in watts/hour
#for various appliances and prompt user to enter the daily hours for
#each appliance. The program then displays the table again with the
#daily hours and calculated value of the total daily energy cost.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - appliance_list
#   - hr_list
#   - hrs_input
#   - total_energy_cost

#START CODING FROM HERE
#======================
#Create a list named appliance_list with the 3 appliances
#shown in the screenshot in Coursemology
appliance_list = [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]]

#Prompt and obtain input for average daily consumption for appliances
hrs_input = '5;4;24'

#Perform Calculation of Total Daily Energy Cost
def calculateEnergyCost(appliance_list,hrs_input):
    total_energy = 0
    total_energy_cost = 0
    #Code to parse the input string in hrs_input (Hint: Use the split() function)
    hr_list = hrs_input.split(';')

    print() #Modify to display list of appliances and daily hours used
    x = 0
    i = 0
    while x != 3:
        
        total_energy = total_energy + (appliance_list[x][1] * int(hr_list[x]) / 1000)
        x+=1

    total_energy_cost = round(total_energy * 0.235,2)

    print("List of Electrical Appliances with Energy in Watts/Hr \n")
    print('{0:<14s}{1:<15s}'.format("Name", "Energy(Watts/Hr)"))
    while i != 3:
        print('{0:<14s}{1:<15d}'.format(str(appliance_list[i][0]),appliance_list[i][1]))
        i+=1
    print("\nEnter hours daily for the above applicances separated by ';' : ")

    i = 0
    print('{0:<14s}{1:<18s}{2:<19s}'.format("Name", "Energy(Watts/Hr)","Daily Hrs used"))
    while i != 3:
        print('{0:<14s}{1:<18d}{2:<19s}'.format(str(appliance_list[i][0]),appliance_list[i][1],hr_list[i]))
        i+=1

    print(f"Total daily energy consumed (kW): {total_energy}") #Modify to display the daily energy consumed
    print(f"Total daily energy cost ($): {total_energy_cost}") #Modify to display the calculated total energy cost

    return total_energy_cost #Do not remove this line

    
#Do not remove the next line
calculateEnergyCost(appliance_list,hrs_input)

#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'5;4;24' output 2.34422
