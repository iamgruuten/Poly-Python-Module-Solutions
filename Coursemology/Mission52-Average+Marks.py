#Programming I

########################
#     Mission 5.2      #
#    Average Marks     #
########################

#Background
#==========
#You are suppose to display all the students and their respective marks
#and to calculate the average mark for these students
#   1) John - 100
#   2) Tom - 75
#   3) Jane - 80
#   4) Jim - 20
#   5) Mary - 50
#   6) Steve - 70
#   7) Anne - 95

#Important Notes
#===============
#You MUST use the following variables
#   - student_list
#   - mark_list
#   - average



#START CODING FROM HERE
#======================

#Create the lists student_list and mark_list
student_list = ['John', 'Tom', 'Jane', 'Jim', 'Mary', 'Steve', 'Anne']
mark_list = [100,75,80,20,50,70,95]


#Calculate and return the average mark
def calculate_average(student_list, mark_list):
    index = 0
    total = 0
    while index != len(student_list):
        print("{0}) {1} - {2}".format(index + 1, student_list[index], mark_list[index]))
        total += mark_list[index]
        index += 1
    average = total / len(student_list)
    print(average)
    return average #Do not remove this line

    
#Do not remove the next line
calculate_average(student_list, mark_list)


#output 70
