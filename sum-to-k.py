def sum_to_k(lst, K):
    pairs = set()

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == K and not in pairs:
                pairs.add(i, j)

    return pairs


