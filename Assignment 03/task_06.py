def process_prices(prices):
    discounted = list(map(lambda x: x - (x * 0.10), prices))
    filtered = list(filter(lambda x: x > 300, discounted))
    return discounted, filtered

print(process_prices([100, 500, 900, 50, 750]))
