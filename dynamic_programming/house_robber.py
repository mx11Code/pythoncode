class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        result_of_each_step = [-1 for i in range(len(A))]
        result_of_each_step[0] = A[0]
        result_of_each_step[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            result_of_each_step[i] = max(result_of_each_step[i - 1], result_of_each_step[i - 2] + A[i])
        return result_of_each_step[len(A) - 1]