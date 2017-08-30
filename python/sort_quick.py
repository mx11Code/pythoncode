def sort_quick(lst):
    if len(lst) == 0:
        return lst  # 1
    first = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        if lst[i] >= first:
            right.append(lst[i])
        else:
            left.append(lst[i])
    return sort_quick(left) + [first] + sort_quick(right)


print(sort_quick([6, 7, 1, 0, 4, 3, 5, 12]))
