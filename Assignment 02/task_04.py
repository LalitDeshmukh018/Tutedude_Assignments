daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily:
    if sale == -1:
        break
    if sale == 0:
        continue

    total_sales += sale
    print("Running Total:", total_sales)

print("Final Total:", total_sales)
