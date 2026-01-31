new_sales = [5000, 2500, 1700]

f = open("sales_data.txt", "a")
for s in new_sales:
    f.write(str(s) + "\n")
f.close()

f = open("sales_data.txt", "r")
lines = f.readlines()
print("".join(lines))
print(len(lines))
f.close()
