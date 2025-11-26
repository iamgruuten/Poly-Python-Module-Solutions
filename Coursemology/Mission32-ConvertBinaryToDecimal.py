#Programming I

################################
#      Mission 3.2             #
#   Convert Binary to Decimal  #
################################


#Write a Python program to convert a given binary
#value to a decimal value
#The program is to prompt user for a binary value
#and display the calculated decimal value.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - binary_value
#   - decimal_value

#START CODING FROM HERE
#======================
#Prompt and obtain input of a 4-digit binary value and assign it to binary_value
#Note: Do not change the input to int type.
#binary_value = input("Input binary value: ")

#Perform Conversion of Binary to Decimal value
def binaryToDecimal(binary_value):
    n = 0
    decimal_value = 0

    while n != len(binary_value):
        
        currentDigit = binary_value[-1-n]
        print(currentDigit) #Modify to display the calculated Decimal value
        decimal_value = decimal_value + ((int(currentDigit)) * 2**n)
        n+=1
        
    print(decimal_value) #Modify to display the calculated Decimal value

    return decimal_value #Do not remove this line

    
#Do not remove the next line
binary_value = '1100'
binaryToDecimal(binary_value)

#input '1011' output 11
#input '1100' output 12
