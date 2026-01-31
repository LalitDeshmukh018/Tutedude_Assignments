gst = lambda price: price + (0.18 * price)
final_price = lambda price, discount: gst(price) - discount

print(gst(100))
