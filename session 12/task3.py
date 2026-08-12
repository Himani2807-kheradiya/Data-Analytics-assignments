products = ['Shoes', 'Mobile Phone', 'Shirt', 'Laptop', 'Smart Watch', 'Headphones']

s_products = list(filter(lambda product: product.lower().startswith('s'), products))

print("Products starting with S:", s_products)