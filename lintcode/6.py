def mergeSortedArray(A, B):
    def sort_quick(lst):
        if len(lst) == 0:
            return lst
        pivot = lst[0]
        left = []
        right = []
        for i in range(1, len(lst)):
            if lst[i] <= pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
        return sort_quick(left) + [pivot] + sort_quick(right)

    A.extend(B)
    return sort_quick(A)
