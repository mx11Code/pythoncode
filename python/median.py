def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2] + lst[len(lst)//2 - 1])/2.0
    else:
        return lst[(len(lst)-1)//2]

print(median([4, 5, 5, 4]))
