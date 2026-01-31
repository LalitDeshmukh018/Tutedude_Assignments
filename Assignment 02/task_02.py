orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders = 0

for order in orders:
    if order >= 2000:
        discount = 0.15
    elif order >= 1500:
        discount = 0.10
    elif order >= 1000:
        discount = 0.07
    else:
        discount = 0

    final_amount = order - (order * discount)
    total_revenue += final_amount

    if discount > 0:
        discounted_orders += 1

    print(order, "->", int(discount * 100), "% ->", final_amount)

print("Total Revenue:", total_revenue)
print("Orders with discount:", discounted_orders)
