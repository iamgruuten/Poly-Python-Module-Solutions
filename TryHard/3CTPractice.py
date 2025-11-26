name = ["John Tan", "Tom Ong", "Jane Lim", "Jim Ng", "Mary Choo", "Steve Goh", "Anne Lee"]
marks = [100,75,80,20,50,70,95]
total = 0
for i in range(len(name)):
    print("{:<14}{}".format(name[i], marks[i]))
    total += marks[i]

average = total / len(name)
print("\nAverage is {}".format(average))
goh = []
for i in range(len(name)):
    if name[i].find('Goh') != -1:
        print("{} score {} marks".format(name[i], marks[i]))
    
