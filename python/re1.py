import re


def func():
    print("Please input your ID number:")
    num = str(input())
    return bool(re.search(r"^([1-8][1-8])(\d{4})(19[0-9]|20[0-1])\d(12+|11+|10?||[2-9])([0-2][0-9])\d{3}0(\d|x)$", num))

print(func())


def func1():
    print("Please input your Email:")
    email = str(input())
    return bool(re.search(r"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,10}\.(com|cn|net)$", email))


print(func1())
