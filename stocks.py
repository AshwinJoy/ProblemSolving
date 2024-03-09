def max_profit(prices):
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


stock_prices1 = list(map(int, input().split(',')))
print(max_profit(stock_prices1))
