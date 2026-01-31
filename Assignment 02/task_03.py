orders = []

while True:
    print("\n1 - Add order")
    print("2 - Show orders")
    print("q - Quit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            amount = int(input("Enter order amount: "))
            orders.append(amount)
        except ValueError:
            print("Invalid amount")
            continue

    elif choice == "2":
        total = 0
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
            total += final_amount
            print(order, "->", final_amount)

        print("Total:", total)

    elif choice == "q":
        break

    else:
        print("Invalid choice")
        continue
