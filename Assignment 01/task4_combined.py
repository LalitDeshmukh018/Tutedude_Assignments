products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones"]

categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics",
    "Accessories"
]

price_dict = {
    "Laptop": 55000,
    "Mouse": 600,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000,
    "Headphones": 2000
}

catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print(catalog)

category_to_products = {}

for item in catalog:
    product = item[0]
    category = item[2]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)

max_category = ""
max_count = 0

for category in category_to_products:
    if len(category_to_products[category]) > max_count:
        max_count = len(category_to_products[category])
        max_category = category

print(category_to_products[max_category])
