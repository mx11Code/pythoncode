class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        x = len(A)
        y = len(B)
        result_of_each_step = [[0 for j in range(y + 1)] for i in range(x + 1)]
        for i in range(x):
            for j in range(y):
                # result_of_each_step[i + 1][j + 1] = max(result_of_each_step[i][j + 1],
                #                                         result_of_each_step[i + 1][j])
                if A[i] == B[j]:
                    result_of_each_step[i + 1][j + 1] = result_of_each_step[i][j] + 1
                else:
                    result_of_each_step[i + 1][j + 1] = max(result_of_each_step[i][j + 1],
                                                            result_of_each_step[i + 1][j])
        return result_of_each_step[x][y]




result = Solution()
print(result.longestCommonSubsequence("ABCD", "EACB"))
