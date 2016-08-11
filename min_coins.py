def min_coins(coins, val):
    for coin in coins:
        coin_count = value/coin
        total_count += coin_count
        value -= coin*coin_count

        return total_count
