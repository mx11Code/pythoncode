def func(lst1, lst2):
    difference_set = []
    for i in lst1:
        if i not in lst2:
            difference_set.append(i)
    return difference_set


print(func([1, 2, 3], [2, 3]))


def func1(lst1, lst2):
    intersection = []
    for i in lst1:
        if i in lst2:
            intersection.append(i)
    return intersection


print(func1([1, 2, 3], [2, 3]))


def func2(lst1, lst2):
    union_set = []
    for i in lst1:
        union_set.append(i)
    for j in lst2:
        if j not in lst1:
            union_set.append(j)
            union_set.sort()
    return union_set


print(func2([1, 2, 4, 5], [2, 3, 5, 6]))
