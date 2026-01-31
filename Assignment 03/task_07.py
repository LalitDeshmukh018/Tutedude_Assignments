def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

prices = []

while True:
    print("1 Add price")
    print("2 Show average price")
    print("3 Show highest price")
    print("q Quit")

    choice = input()

    if choice == "1":
        price = int(input())
        add_price(prices, price)

    elif choice == "2":
        if prices:
            print(get_average_price(prices))
        else:
            print("No prices")

    elif choice == "3":
        if prices:
            print(get_max_price(prices))
        else:
            print("No prices")

    elif choice == "q":
        break
