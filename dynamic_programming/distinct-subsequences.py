class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        if m == 0:
            return 0
        record = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            record[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    record[i][j] = record[i - 1][j] + record[i - 1][j - 1]
                else:
                    record[i][j] = record[i - 1][j]
        print(record)
        return record[m][n]


result = Solution()
print(result.numDistinct("rabbbit", "rabbit"))