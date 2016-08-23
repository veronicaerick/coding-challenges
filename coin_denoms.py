def change_possibilities(amount, denoms):
    # 
    ways_of_doing_cents = [0] * (amount +1)
    ways_of_doing_cents[0] = 1

    for coin in denoms:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_cents[higher_amount] += ways_of_doing_cents[higher_amount_remainder]

    return ways_of_doing_cents[amount]