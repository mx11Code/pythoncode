class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return None
        # 每一次运算记录最大值和最小值，最小值放在第一位，最大值放在第二位
        record = [[0, 0] for i in range(n)]
        # 初始化第一个记录
        record[0] = [nums[0], nums[0]]
        max_value = nums[0]
        # 从第二个元素开始计算
        for i in range(1, n):
            # 一个可能的最值（最大最小不知）
            t1 = record[i - 1][0] * nums[i]
            # 另一个可能的最值（最大最小不知）
            t2 = record[i - 1][1] * nums[i]
            # 最小值
            record[i][0] = min(nums[i], t1, t2)
            # 最大值
            record[i][1] = max(nums[i], t1, t2)
            # 最大值比较函数
            max_value = max(record[i][1], max_value)
        return max_value
