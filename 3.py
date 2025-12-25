# Puzzle input
prices = [139, 127, 130, 148, 158, 178, 195, 179, 197, 177, 187]

min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        max_profit = max(max_profit, price - min_price)

print(max_profit)
