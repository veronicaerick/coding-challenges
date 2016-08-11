def get_max_stock(prices):
    max_profit = 0

    for outer_time in xrange(len(prices)):
        for inner_time in x range(len(prices)):
            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)

            earlier_price = prices[earlier_time]
            later_price = prices[later_time]

            potential_profit = later_price - earlier_price

            max_profit = max(max_profit, potential_profit)

    return max_profit

#  run time is O(n2)

def get_max_stock_v2(prices):
    max_profit = 0
    # go throygh all prices, with index as time
    for earlier_time, earlier_price in enumerate(prices):
            for later_price in prices[earlier_time+1:]:
                potential_profit = later_price -earlier_price

                max_profit = max(max_profit, potential_profit)

    return max_profit

  def get_max_profit_v3(stock_prices_yesterday):

    min_price = stock_prices_yesterday[0]
    max_profit = 0

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit