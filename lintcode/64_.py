def mergeSortedArray(A, m, B, n):
    # write your code here
    for i in range(n):
        A[i + m] = B[i]
    A.sort()
