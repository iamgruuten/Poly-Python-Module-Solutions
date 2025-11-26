#ProcessMarks lists
def ProcessMarks(markLists):
    print(f"The 1st element is {markLists[0]}") #Display 1st element
    sum = markLists[-1] + markLists[-2] #Assigning sum values to variable
    print(f"The sum of last 2 elements is {sum}") #Display sum of last 2 element
    print(f"Double value of 2nd element is {2 * markLists[1]}") #Display double value of 2nd element
    
markLists = [89, 77, 55, 69, 50, 60, 11, 10, 14, 20] #This is the list of marks
ProcessMarks(markLists)
