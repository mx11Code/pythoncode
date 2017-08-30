def func(n):
    fn = [0, 1]
    for i in range(2, n+1):
        fn.append(i + fn[i - 1])
    return fn[n]


print(func(100))
