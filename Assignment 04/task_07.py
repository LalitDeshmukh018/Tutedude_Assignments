prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = int(input())

f = open("discount_report.txt", "w")

total_items = 0
total_discounted = 0

for product in prices:
    original = prices[product]
    discounted = original - (original * discount / 100)
    f.write(product + " | " + str(original) + " | " + str(int(discounted)) + "\n")
    total_items += 1
    total_discounted += discounted

average_discounted = total_discounted / total_items
f.write("Total Items: " + str(total_items) + "\n")
f.write("Average Discounted Price: " + str(int(average_discounted)) + "\n")

f.close()

f = open("discount_report.txt", "r")
print(f.read())
f.close()
