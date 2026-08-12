# Task 2: Clean brand name

def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name

brand = clean_brand_name(" oneplus-Nord ")

print(brand)