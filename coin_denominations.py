def change_possib(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amt in xrange(coin, amount + 1):
            higher_amt_remainder = higher_amt - coin
            ways_of_doing_n_cents[higher_amt] += ways_of_doing_n_cents[higher_amt_remainder]

        return ways_of_doing_n_cents[amount]