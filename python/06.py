# 1, 2, 1+2=3, 2+3=5, 3+5=8,
# n! = n * (n-1)!


# def factorial(n):
#     val = 1
#     for i in range(1, n+1):
#         val = val * i
#     return val
#
# val1 = factorial(4)
# print(val1)
#
#
def factorial1(n):
    if n == 0:
        return 1
    return n * factorial1(n - 1)


val1 = factorial1(100)
print(val1)

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)
#
# sum1 = sum(100)
# print(sum1)

d = {}


def fibonacci(n):
    if n in d:
        return d[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    val = fibonacci(n - 1) + fibonacci(n - 2)
    d[n] = val
    return val


print(fibonacci(100))


def fibonacci2(n):
    fn = [0, 1, 2]
    for i in range(3, n + 1):
        fn.append(fn[i - 1] + fn[i - 2])
    return fn[n]


print(fibonacci2(100))
