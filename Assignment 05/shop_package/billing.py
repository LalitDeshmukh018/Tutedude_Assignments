from .discount import apply_discount, flat_discount

def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    return amount + (amount * 0.05)

