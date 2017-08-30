class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def get_longest(self, lst):
        length = []
        count = 1
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                count += 1
            else:
                length.append(count)
                count = 1
                continue

            length.append(count)
        return max(length)

    # result = Solution()
    # print(result.get_longest([5, 4, 3, 1, 2]))


    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        return max(self.get_longest(A), self.get_longest(list(reversed(A))))


result = Solution()
print(result.longestIncreasingContinuousSubsequence([10, 9, 7, 8, 6, 5, 4, 1, 2]))


class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def get_longest(self, lst):
        result_of_each_step = [1 for i in range(len(lst))]
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                result_of_each_step[i + 1] = result_of_each_step[i] + 1
        return max(result_of_each_step)

    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        return max(self.get_longest(A), self.get_longest(list(reversed(A))))
