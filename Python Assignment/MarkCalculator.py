'''

input: Marks for each test
process: Calculate ct * 0.3 + assign * 0.3 + asses *0.4
output: show total percentage

To find the final mark achieved by the students
In order to find the percentage achieved by students:
Common_test percentage = 30%
Assignment Percentage = 30%
Assesment percentage = 40%

To find the percentage of the student achieved
Taking the students score and multiply the percentage

75 * 40%
80 * 30%
60 * 30%
Add the above results

'''




#Calculate the total percentage that the student scored

def final_mark(ct, assign, asses):
    ct_percent = ct * 0.3
    assign_percent = assign * 0.3
    asses_percent = asses * 0.4
    total_percent = ct_percent + assign_percent + asses_percent
    print(f"Your total percentage is {str(total_percent)}")


common_test = float(input("Enter Common Test Mark: "))
assignment = float(input("Enter Assignment Mark: "))
assesment = float(input("Enter Assessment Mark: "))
final_mark(common_test, assignment, assesment)

