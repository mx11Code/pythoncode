def isUnique(str):
    # write your code here
    counter = {}
    for char in str:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return False
    return True