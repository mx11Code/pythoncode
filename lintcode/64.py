def mergeSortedArray(A, m, B, n):
    # write your code here
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

    for i in range(n):
        A[i + m] = B[i]
    return sort_quick(A)

print(mergeSortedArray([1, 3, 4, 6, 0, 0], 4, [2, 5], 2))
