def func(lst, i, n):
    lst.append(None)
    for j in range(len(lst) - 1, i - 1, -1):
        lst[j] = lst[j - 1]
    lst[i] = n


lst = [1, 2, 3]
func(lst, 1, 5)
print(lst)


def swap(lst, pos1, pos2):
    tmp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = tmp


def func(lst, i, n):
    lst.append(None)

    for c in range(len(lst) - 1, i, -1):
        swap(lst, c, c - 1)

    lst[i] = n


lst = [6, 7, 8]
func(lst, 0, 3)
print(lst)
