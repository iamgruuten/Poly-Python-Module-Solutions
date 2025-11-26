item = ['Apple Pie', 'Chicken Pie', 'Apple Tart', 'Egg Tart', 'Durian Tart']
price = [1.80, 2.90, 0.85, 0.95, 1.10]
quantity = [3,5,9,12,30]
total = 0
for i in range(len(item)):
    total += float(price[i]) * float(quantity[i])

print('Your total cost is ${:.2f}'.format(total))

print("{:<20}{:<15}{}".format("Item", "Unit Price", "Quantity"))
print("{:<20}{:<15}{} \n".format("====", "==========", "==========="))

for i in range(len(item)):
    print("{:<20}${:<15.2f}{}".format(item[i], price[i], quantity[i]))
