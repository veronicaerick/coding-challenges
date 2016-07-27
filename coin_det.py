# Have the function CoinDeterminer(num) take the input,
# which will be an integer ranging from 1 to 250, and return an
# integer output that will specify the least number of coins, that when
#added, equal the input integer. Coins are based on a system as follows:
# there are coins representing the integers 1, 5, 7, 9, and 11.
# So for example: if num is 16, then the output should be 2 because you
# can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins.

def coin_determiner(num):
    coins = [1,5,7,9,11]
    coin_dict = {}

    for coin in coins:
        coin_dict[coin] = 1

    def coin_helper(num):
        if num in coin_dict:
            return coin_dict[num]

        else:
            possibilities = []
            A = num - 1
            B = num - A

            while A => num/2:
                possibilities.append(coin_helper(A)) + coin_helper(B))
                A -= 1
                b += 1
