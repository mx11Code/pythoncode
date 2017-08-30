def reverseInteger(n):
    if n == 0:
        return 0
    str1 = str(n)
    if len(str1) >= 10:
        return 0
    if str1[0] != "-":
        return int(str1[::-1])
    elif str1[0] == "-":
        str2 = str1[1:]
        return int(str1[0] + str2[::-1])
