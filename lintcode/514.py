def numWays(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return k
    if n > 2 and k == 1:
        return 0
    if n >= 2:
        same_color = k
        diff_color = k * (k - 1)
        for i in range(2, n):
            temp = diff_color
            diff_color = (same_color + diff_color) * (k - 1)
            same_color = temp
        return same_color + diff_color
