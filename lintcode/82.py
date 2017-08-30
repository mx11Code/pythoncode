def singleNumber(A):
    if len(A) == 0:
        return 0
    counter = {}
    for item in A:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    for item in counter:
        if counter[item] == 1:
            return item
