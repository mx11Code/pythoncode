class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        # Write your code here
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        if n > 2 and k == 1:
            return 0
        if n <= 2 and k == 1:
            return 1
        if n >= 2:
            result_of_each_step = [-1 for i in range(n)]
            result_of_each_step[0] = k
            result_of_each_step[1] = k * k
            for i in range(2, n):
                result_of_each_step[i] = (k - 1) * (result_of_each_step[i - 1] + result_of_each_step[i - 2])
            return result_of_each_step[n - 1]