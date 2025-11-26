def find_larger(num1 , num2):
    large = num1 if (num1 > num2) else num2
    return large

int1 = input("Enter 1st integer: ")
int2 = input("Enter 2nd integer: ")
int3 = input("Enter 3rd integer: ")
int4 = input("Enter 4th integer: ")

highest1 = find_larger(int1, int2)
highest2 = find_larger(int3, int4)
highest = find_larger(highest1, highest2)

print("The largest integer is " + highest)
