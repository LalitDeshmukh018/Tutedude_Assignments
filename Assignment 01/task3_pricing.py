price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000,
    "Headphones": 2000
}

price_dict["Webcam"] = 2500

price_dict["Mouse"] = 600

name = "Speaker"

if name in price_dict:
    del price_dict[name]
else:
    print("Product not found")

total = 0

for price in price_dict.values():
    total = total + price

average = total / len(price_dict)
print(average)

print(max(price_dict, key=price_dict.get))
print(min(price_dict, key=price_dict.get))
