'''
input: gst, price
process: total = price*gst +price
output: show total cost

'''

#To calculate the total cost including GST

def totalcost(price):
    gst = 0.07
    gst_item = price * gst
    total = price + gst_item
    print(f"Total cost is {str(total)}")

itemcost = float(250)
totalcost(itemcost)

