class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if self.iseven(nums[left]):
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums

    def iseven(self, n):
        return n % 2 == 0