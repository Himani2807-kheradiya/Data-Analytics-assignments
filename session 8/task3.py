item_prices = [299, 499, 199, 999, 149]

total = 0

for price in item_prices:
    if price < 200:
        continue

    total = total + price

print("Total of remaining items:", total)