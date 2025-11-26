import math

vehicle_type = input("Enter vehicle type [Car/Motorcycle]: ")
entry_time = float(input("Enter entry time: "))
exit_time = float(input("Enter exit time: "))

duration = math.ceil(exit_time - entry_time)

if vehicle_type.upper() == "CAR":
    cost = 1.2

elif vehicle_type.upper() == "MOTORCYCLE":
    cost = 0.65

print("Duration : {:.0f}hours".format(duration))
charges = duration * cost
print("The charges for your {} is ${:.2f}".format(vehicle_type, charges))
