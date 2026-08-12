# Task 3: Extract brand and model

product = "Apple iPhone 14 Pro Max"

words = product.split()

brand = product[:product.find(" ")]
model = product[product.find(" ") + 1:]

print("Brand:", brand)
print("Model:", model)