def max_profit(prices):
    min_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        current_profit = prices[i] - min_price

        if current_profit > profit:
            profit = current_profit

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))


# 5