# 从上到下
class Solution:
    def path_sum(self, x, y):
        if x == 0 and y == 0:
            return self.grid[0][0]
        cache_key = str(x) + "," + str(y)
        if cache_key in self.cache:
            return self.cache[cache_key]
        possible = []
        if x >= 1:
            possible.append(self.path_sum(x - 1, y))
        if y >= 1:
            possible.append(self.path_sum(x, y - 1))
        r = min(possible) + self.grid[x][y]
        self.cache[cache_key] = r
        return r

    def min_path_sum(self, grid):
        self.grid = grid
        self.cache = {}
        row_index = len(grid) - 1
        col_index = len(grid[0]) - 1
        return self.path_sum(row_index, col_index)


result = Solution()
print(result.min_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# 从下到上
def min_path_sum(x, y, grid):
    m = len(grid)
    n = len(grid[0])
    result_of_each_step = [[-1 for i in range(n)] for i in range(m)]
    result_of_each_step[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            candidates = []
            if i >= 1:
                candidates.append(result_of_each_step[i - 1][j])
            if j >= 1:
                candidates.append(result_of_each_step[i][j - 1])
            if not candidates:
                candidates = [0]
            result_of_each_step[i][j] = min(candidates) + grid[i][j]
    return result_of_each_step[x][y]


print(min_path_sum(2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
