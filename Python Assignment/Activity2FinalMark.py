#Calculate the total percentage that the student scored

def final_mark(ct, assign, asses):
    ct_percent = ct * 0.3
    assign_percent = assign * 0.3
    asses_percent = asses * 0.4
    total_percent = ct_percent + assign_percent + asses_percent
    print('{:<12s}{:<7s}{:<7s}{:<7s}{:<7s}'.format("StudentNo", "Test", "Assgn", "CA", "Final"))
    print('{:<12d}{:<7.0f}{:<7.0f}{:<7.2f}{:<7.2f}'.format(StudentNo, ct, assign, asses, total_percent))

StudentNo = int(input("Enter StudentNo: "))
common_test = float(input("Enter Common Test Mark: "))
assignment = float(input("Enter Assignment Mark: "))
assesment = float(input("Enter Assessment Mark: "))
final_mark(common_test, assignment, assesment)
