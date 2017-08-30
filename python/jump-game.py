class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        cur, far = 0, 0
        n = len(A)
        while cur < n:
            if far >= n-1:
                return True
            elif cur > far:
                return False
            far = max(far, cur + A[cur])
            cur += 1