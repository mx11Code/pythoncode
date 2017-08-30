def func(arr):
    n = len(arr)
    m = [1] * n
    for x in range(n - 1, 0, -1):
        for y in range(x - 1, -1, -1):
            if arr[y] > arr[x] and m[y] <= m[x]:
                m[y] += 1
    return max(m)


arr = [389, 207, 155, 300, 299, 170, 158, 65]
print(func(arr))
