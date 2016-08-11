def three_sum(lst, K):
    int_dict = {}
    int_set = set(lst)
    results = []

    for i, num in enumerate(lst):
        int_dict.setdefault(num, []).append(i)

    for i in range(len(lst)):
        for i in range(i+1, len(lst)):
            diff = K - lst[i] + lst[j]
            if K - diff in int_set:
                return i, j, [k - diff][0]

def two_sum(array, S):
    pairs = set()

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if lst[i] + lst[j] == S and i, j not in pairs:
                pairs.add(i,j)

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
