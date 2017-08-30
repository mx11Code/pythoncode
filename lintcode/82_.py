def singleNumber(A):
    # write your code here
    ans = 0
    for x in A:
        ans = ans ^ x
    return ans
