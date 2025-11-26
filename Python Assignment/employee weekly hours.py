employee_list = ['Jenny','Luke','Mike','Joanne','Tom']
title = ["Employee Name", "Total Hrs in Week", "Total Salary($)"]
hrs_list= [[2, 4, 3, 4, 5, 8, 8],\
[7, 3, 4, 3, 3, 4, 4],\
[3, 3, 4, 3, 3, 2, 2],\
[9, 3, 4, 7, 3, 4, 1],\
[3, 5, 4, 3, 6, 3, 8]]

days = ["Su", "M", "T", "W", "Th", "F", "Sa"]

print("Work Hours Processing")
print("=" * 20)

menu_options = ["Working Hrs in the week", "Total Hrs and Salary by Employee", "Total Hrs by Day", "Edit Working Hrs", "Exit"]

def show_menu():
    print()
    index = 0
    for i in menu_options:
        index += 1
        print("[{}] {}".format(index , i))
    print()
def working_hrs():
    print("{:<8}".format(" "), end="")
    for a in days:
        print("{:>5}".format(a), end="")

    print()

    for b in range(len(employee_list)):
        print("{:<8}".format(employee_list[b]), end="")
        for i in hrs_list[b]:
            print("{:>5}".format(i), end="")
        print()

    
    
 

def totalHrandSalary():
    print("Total Hrs and Salary by Employee")
    grand_tt = 0
    for i in title:
        print("{:<20}".format(i), end="")

    print()
    
    for b in range(len(employee_list)):
        print("{:<20}".format(employee_list[b]), end="")
        total = 0

        
        
        for k in hrs_list[b]:
            total += k
        grand_tt += total
        print("{:<20}".format(total), end="")
        print("{:<20}".format(total * 5), end="")
        print()
        
    print("Total Hrs Worked: {}".format(grand_tt))
    print("Total Salary to be paid($): {}".format(grand_tt*5))

def totalhrsbyday():
    for a in days:
        print("{:<5}".format(a), end="")
    print()
    

    init = 0;
    total = 0;
    
    for i in range(len(hrs_list[0])):
        total = 0
        for a in range(len(hrs_list)): 
            total += hrs_list[a][i]
        print("{:<5}".format(total), end="")
            
                       


def edithours():

    working_hrs()

    name = input("Please enter the employee name to edit: ")
    day = input("Please enter the day to edit: ")
    new_hours = input("Please enter the new working hours: ")

    name_index = employee_list.index(name)
    day_index = days.index(day)

    hrs_list[name_index][day_index] = new_hours

    print("Edit completed")
    

while True:
    show_menu()
    option = int(input("Enter option: "))
    if option == 1:working_hrs()
    elif option == 2:totalHrandSalary()
    elif option == 3:totalhrsbyday()
    elif option == 4:edithours()
    elif option == 5:break;

        
        
    
    
