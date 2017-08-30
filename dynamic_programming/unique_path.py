# 从上到下
cache = {}


def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    cache_key = str(m) + "," + str(n)
    if cache_key in cache:
        return cache

    candidates = []
    if m >= 2:
        candidates.append(unique_paths(m - 1, n))
    if n >= 2:
        candidates.append(unique_paths(m, n - 1))

    result = sum(candidates)
    cache[cache_key] = result
    return result


print(unique_paths(1, 3))
# 从下到上
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def unique_path(self, m, n):
        x = m - 1
        y = n - 1

        result_of_each_step = [[-1 for c in range(y + 1)] for r in range(x + 1)]
        for i in range(0, m):
            result_of_each_step[i][0] = 1
        for i in range(0, n):
            result_of_each_step[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                candidates = [result_of_each_step[i - 1][j], result_of_each_step[i][j - 1]]
                result_of_each_step[i][j] = sum(candidates)
        return result_of_each_step[x][y]


result = Solution()
print(result.unique_path(2, 3))