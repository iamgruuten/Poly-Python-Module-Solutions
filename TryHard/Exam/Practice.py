score = '90;20;30;10;50;60;100'
student = 'jack;max;jane;john;mary;corny;terry'

new_score = score.split(';')
print(new_score)
new_student = student.split(';')

#This will capitalize every name in list
for x in new_student:
    finder = new_student.index(x)
    new_student[finder] = x.capitalize()

new_student.sort()
print(new_student)

