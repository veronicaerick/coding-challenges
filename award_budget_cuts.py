# planned to give g grants
# reduced to b dollars
# apply a cap, everything higher than c will be capped at c


# given an array of grants (g), and a (b) budget- find the
#  cap (c)

# sort the
def budget_cuts(g,b):
    grants = length(g)
    partial_sums = []
    temp_sum = 0

    for i in range(len(n) -1):
        temp_sum = temp_sum + g[i]
        partial_sums[i] = temp_sum
    if (partial_sums[n-1] <= b):
        return g[n-1]

