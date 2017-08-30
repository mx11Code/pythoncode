class Solution:
    # param matrix: a matrix of 0 and 1
    # return: an integer
    def maxSquare(self, matrix):
        # write your code here
        x = len(matrix)
        y = len(matrix[0])
        result_of_each_step = [[-1 for j in range(y)] for i in range(x)]
        for i in range(x):
            result_of_each_step[i][0] = matrix[i][0]
        for j in range(y):
            result_of_each_step[0][j] = matrix[0][j]
        for i in range(1, x):
            for j in range(1, y):
                if matrix[i][j] == 0:
                    result_of_each_step[i][j] = 0
                else:
                    result_of_each_step[i][j] = min(result_of_each_step[i - 1][j - 1], result_of_each_step[i - 1][j],
                                                    result_of_each_step[i][j - 1]) + matrix[i][j]
        ans = 0
        for i in range(x):
            for j in range(y):
                ans = max(ans, result_of_each_step[i][j])
        return ans * ans
