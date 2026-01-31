order_amount = int(input("Enter order amount: "))

if order_amount >= 2000:
        discount = 0.15
elif order_amount >= 1500:
        discount = 0.10
elif order_amount >= 1000:
        discount = 0.07
else:
        discount = 0

subtotal = order_amount - (order_amount * discount)
tax = subtotal * 0.05
final_amount = subtotal + tax
print("Subtotal:", subtotal)
print("Tax:", tax)
print("Final Amount:", final_amount)


