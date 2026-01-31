prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError
        if price < 0:
            raise ValueError("Negative price not allowed")
        total += price
    except TypeError:
        print("Invalid item skipped")
    except ValueError as e:
        print(e)

print("Total bill:", total)
