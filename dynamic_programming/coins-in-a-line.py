class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        result_of_each_step = [False for i in range(max(n + 1, 3))]
        result_of_each_step[1] = True
        result_of_each_step[2] = True
        m = 2
        for i in range(3, n + 1):
            result_of_each_step[i] = True if result_of_each_step[i - m - 1] == True else False
        return result_of_each_step[n]


result = Solution()
print(result.firstWillWin(9999))
