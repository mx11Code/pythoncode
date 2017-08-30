def removeElement(A, elem):
    # write your code here
    j = len(A) - 1
    for i in range(len(A)-1, -1, -1):
        if A[i] == elem:
            A[i], A[j] = A[j], A[i]
            j -= 1
    return j + 1