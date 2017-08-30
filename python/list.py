def func(lst, i, x):
    lst.append(None)
    for j in range(len(lst) - 1, i - 1, -1):
        lst[j] = lst[j - 1]
    lst[i] = x


lst = [1, 2, 3]
func(lst, 1, 5)
print(lst)
