def func(arr):
    fn = [1]
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            fn.append(fn[i - 1] + 1)
        else:
            fn.append(1)
    return max(fn)

arr = [389, 207, 155, 300, 299, 170, 158, 65]
print(func(arr))
