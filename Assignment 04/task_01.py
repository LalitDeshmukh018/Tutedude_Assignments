sales = [1200, 450, 980, 1500, 3000]

f = open("sales_data.txt", "w")
for s in sales:
    f.write(str(s) + "\n")
f.close()

f = open("sales_data.txt", "r")
print(f.read())
f.close()
