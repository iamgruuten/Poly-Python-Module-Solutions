value = str(input("Please enter your program in a string: "))

right = 0
left = 0
trace = True
for i in range(len(value)):
    if value[i] == "(":
        right += 1
        continue
    elif value[i] == ")":
        if right > left:
            left += 1
            continue
        else:
            trace = False
            break
if right == left and trace != False:
    print("The program has a balanced delimiters")
else:
    print("The program does not have balanced delimiters")
