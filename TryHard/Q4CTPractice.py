skipped = 0
while 1 > skipped or 100 < skipped:
    skipped = float(input("Enter a number between 1 and 100: "))

for i in range(1, 100):
    if (i % skipped) == 0:
        print("skip")
        continue
    else:
        print(i)
