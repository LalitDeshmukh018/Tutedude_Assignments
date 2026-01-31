f = open("sales_data.txt", "r")
print(f.read())
f.close()

f = open("sales_data.txt", "r")
print(f.readline())
f.close()

f = open("sales_data.txt", "r")
lines = f.readlines()
numbers = []
for line in lines:
    numbers.append(int(line.strip()))
print(numbers)
f.close()
