class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))

    def rob_line(self, A):
        result_of_each_step = [-1 for i in range(len(A))]
        result_of_each_step[0] = A[0]
        result_of_each_step[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            result_of_each_step[i] = max(result_of_each_step[i - 1],
                                         A[i] + result_of_each_step[i - 2])
        return result_of_each_step[len(A) - 1]

