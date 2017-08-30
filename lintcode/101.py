def removeDuplicates(A):
    # write your code here
    if len(A) == 0:
        return len(A)
    counter = {}
    for item in A:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    keys = list(counter.keys())
    keys.sort()
    del A[:]
    for key in keys:
        A.append(key)
        if counter[key] >= 2:
            A.append(key)
    return len(A)
