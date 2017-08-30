class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, grid):
        x = len(grid) - 1
        y = len(grid[0]) - 1

        if grid[0][0] == 1:
            return 0

        result_of_each_step = [[-1 for c in range(y + 1)] for r in range(x + 1)]
        result_of_each_step[0][0] = 1

        for i in range(0, x + 1):
            for j in range(0, y + 1):
                if i == 0 and j == 0:
                    continue

                if grid[i][j] == 1:
                    result_of_each_step[i][j] = 0
                else:
                    candidates = []
                    if i >= 1:
                        candidates.append(result_of_each_step[i - 1][j])

                    if j >= 1:
                        candidates.append(result_of_each_step[i][j - 1])
                    result_of_each_step[i][j] = sum(candidates)

        return result_of_each_step[x][y]


result = Solution()
print(result.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
