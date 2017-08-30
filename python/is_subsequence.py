class Solution():
    def is_subsequence(self, S, T):
        i = 0
        j = 0
        while i < len(S) and j < len(T):
            if S[i] == T[j]:
                i += 1
            j += 1
        return i == len(S)


result = Solution()
print(result.is_subsequence("axc", "ahbgdc"))