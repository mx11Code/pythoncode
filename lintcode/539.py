def moveZeroes(nums):
    count = len(nums)
    while 0 in nums:
        nums.remove(0)
    while len(nums) < count:
        nums.append(0)
    return nums
