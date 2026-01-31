products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones"]

categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics",
    "Accessories"
]

categories_set = set(categories)
print(categories_set)

categories_set.add("Office")
categories_set.add("Accessories")

print(categories_set)

print("Electronics" in categories_set)

print(len(categories_set))
