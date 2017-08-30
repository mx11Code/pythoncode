def compareStrings(A, B):
    # write your code here
    if len(B) == 0:
        return True
    if len(A) == 0:
        return False
    trackTable = [0 for _ in range(26)]
    for i in A:
        trackTable[ord(i) - 65] += 1
    for i in B:
        if trackTable[ord(i) - 65] == 0:
            return False
        else:
            trackTable[ord(i) - 65] -= 1
    return True


print(compareStrings("ABCD", "ACD"))
