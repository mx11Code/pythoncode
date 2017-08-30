def fibonacci(n):
    result_of_each_step = [-1 for i in range(n + 1)]
    result_of_each_step[0] = 0
    result_of_each_step[1] = 1
    result_of_each_step[2] = 2
    for i in range(3, n + 1):
        result_of_each_step[i] = result_of_each_step[i - 1] + result_of_each_step[i - 2]
    return result_of_each_step[n]


cache = {}


def fib2(n):
    if n in cache:
        return cache[n]

    r = n if n <= 3 else fib2(n - 1) + fib2(n - 2)
    cache[n] = r
    return r


print(fibonacci(100) == fib2(100))
