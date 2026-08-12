from functools import reduce

order_amounts = [120, 340, 560, 80]

total_bill = reduce(lambda x, y: x + y, order_amounts)

print("Total Bill Amount:", total_bill)