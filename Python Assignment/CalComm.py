'''
user input sales

if sales > 100000 then
    commission will be 10%
else then
    comission will 5%
ENDIF
'''

def calcomm(sales):
    if int(sales) >= 10000:
        commission = 10
    else:
        commission = 5

    paid = float(sales) * (commission / 100)
    print("The commission rate is : {:.0f}%".format(commission))
    print("The commission paid is : ${:.2f}".format(paid))

sales = input("Enter monthly sales of sales agent: ")
calcomm(sales)
