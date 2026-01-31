f = open("products.txt", "w")

for i in range(3):
    name = input()
    price = input()
    f.write(name + " | " + price + "\n")

f.close()

f = open("products.txt", "r")
for line in f:
    print(line.strip())
f.close()
