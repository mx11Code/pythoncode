def compareStrings(A, B):
    # write your code here
    counter_A = {}
    counter_B = {}
    if len(B) == 0:
        return True
    if len(A) == 0:
        return False
    for char_A in A:
        if char_A in counter_A:
            counter_A[char_A] += 1
        else:
            counter_A[char_A] = 1
    for char_B in B:
        if char_B in counter_B:
            counter_B[char_B] += 1
        else:
            counter_B[char_B] = 1
    print(counter_A)
    print(counter_B)
    count = 0
    for item in counter_B:
        if item not in counter_A:
            return False
        elif counter_B[item] <= counter_A[item]:
            count += 1
    return count == len(counter_B)
