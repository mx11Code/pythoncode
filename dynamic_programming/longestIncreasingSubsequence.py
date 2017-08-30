class Solution():
    def longestIncreasingSubsequence(self, nums):
        x = len(nums)
        if not nums:
            return 0
        result_of_each_step = [1 for i in range(x)]
        for i in range(1, x):
            for j in range(i):
                if (nums[i] > nums[j]) and result_of_each_step[i] < result_of_each_step[j] + 1:
                    result_of_each_step[i] = result_of_each_step[j] + 1
        return max(result_of_each_step)


result = Solution()
print(result.longestIncreasingSubsequence(
    [9, 3, 6, 2, 7]))
