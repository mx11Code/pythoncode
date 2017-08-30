class Solution():
    def minimumTotal(self, triangle):
        x = len(triangle)
        result_of_each_step = [[-1 for j in range(i + 1)] for i in range(x)]
        for j in range(x):
            result_of_each_step[x - 1][j] = triangle[x - 1][j]
        for i in range(x - 2, -1, -1):
            for j in range(i + 1):
                result_of_each_step[i][j] = min(result_of_each_step[i+1][j], result_of_each_step[i+1][j+1]) + \
                                                    triangle[i][j]
        return result_of_each_step[0][0]


result = Solution()
print(result.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
