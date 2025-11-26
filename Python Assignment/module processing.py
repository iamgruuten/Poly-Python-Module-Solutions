p01 = [86,80,75,82,80,70]
p02 = [40,55,60,48,50]
p03 = [90, 85, 30,86,78,75,54]

mark_list = [p01,p02,p03]

print("{:<8}{:<8}".format("Class", "Average"))
grand_total = 0
student_total = 0
highest = mark_list[1][1]
lowest = mark_list[1][1]

for i in mark_list:
    total = 0
    for j in i:
        total += j
        grand_total += j
        if j > highest:
            highest = j
        if j < lowest:
            lowest = j
            
        
    student_total += len(i)
    print("{:<8s}{:<8.2f}".format("P0" + str(mark_list.index(i)+1), total / len(i)))

average = grand_total / student_total
print("The overall average mark is {:.2f}".format(average))
print("The highest mark is {:.0f}".format(highest))
print("The lowest mark is {:.0f}".format(lowest))


    
    

    
    
        
