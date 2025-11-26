# User input original string and substring to delete
# Remove the first occurrence of the substring from the string
# Display the modified string
# Making use of remove function

def deletestring(text):
    textdestroyer = input('Substring to delete : ') #Input string to delete
    text = text.replace(textdestroyer, '', 1)

    return text #return value do not remove

print("\n" + deletestring(input("Enter original string : "))) #Input original string
