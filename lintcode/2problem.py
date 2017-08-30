def trailingZeros(n):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    digit = factorial(n)
    print(digit)
    count = 0
    while digit % 10 == 0:
        count += 1
        digit /= 10
    return count


print(trailingZeros())


# import requests
#
# wd = "今天天气"
# r = requests.get("https://www.baidu.com/s?wd="+wd)
# info = extract(r)
# print(info)
