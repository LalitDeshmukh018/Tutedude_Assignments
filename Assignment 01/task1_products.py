products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones"]

sample_product = ("Laptop", 55000, "Electronics")

print(products[1])
print(products[-1])

products.append("Webcam")
products.append("Speaker")

print(products)

temp = list(sample_product)
temp[1] = 52000
sample_product = tuple(temp)

print(sample_product)

