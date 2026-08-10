product_prices = ['199.99', '299.50', '150']

prices = [float(price) for price in product_prices]

total_cart_value = sum(prices)

print("Product Prices:", prices)
print("Total Cart Value: ₹", total_cart_value)