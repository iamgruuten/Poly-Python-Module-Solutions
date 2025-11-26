#Programming I

####################################
#            Mission 3.2           #
#           Caesar Cipher          #
####################################

#Background
#==========
#The encryption of a plaintext by Caesar Cipher is:
#En(Mi) = (Mi + n) mod 26 

#Write a Python program that prompts user to enter a plaintext
#and displays the encrypted result using Caesar Cipher.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - plaintext
#   - ciphertext

#START CODING FROM HERE
#======================
plaintext = ""
key = ""


#Perform Encryption of given plaintext
def caesarEncrypt(plaintext, key):
    #Code to do the conversion
    ciphertext = ""

    for ch in plaintext:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + int(key) 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        ciphertext += finalLetter
    
    print(ciphertext) #Modify to display the encrypted result

    return ciphertext #Do not remove this line


plaintext = input("Enter the plaintext: ")
key = input("Enter the number of positions to be shifted: ")
#Do not remove the next line
caesarEncrypt(plaintext,key)

