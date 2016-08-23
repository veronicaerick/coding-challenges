def get_max_profit(prices_yesterday):
    min_price = prices_yesterday[0]
    max_price = 0 

    for current_price in prices_yesterday:
        min_price = min(current_price, min_price)
        potential_profit = current_price - min_price
        max_price = max(current_price, max_price)

    return max_price