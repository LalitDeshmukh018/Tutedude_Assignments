f = open("sales_data.txt", "r")
sales = []
for line in f:
    sales.append(int(line.strip()))
f.close()

total = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total / len(sales)

print(total)
print(highest)
print(lowest)
print(average)
