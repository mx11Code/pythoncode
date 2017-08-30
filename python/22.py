def swap(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp


def rotate_string(s, offset):
    x = offset
    lst = [" "] * len(s)
    new_s = [i for i in s]
    for i in range(x):
        lst[i] = new_s[-(x - i)]
    for i in range(x, len(s)):
        lst[i] = new_s[i - x]
    result = "".join(lst)
    return result


print(rotate_string("abcdefg", 1))
