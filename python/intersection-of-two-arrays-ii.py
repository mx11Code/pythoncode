class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        lst = []
        counter = {}
        for i in nums1:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        for j in nums2:
            if j in counter and counter[j] > 0:
                lst.append(j)
                counter[j] -= 1
        return lst


result = Solution()
print(result.intersection([1, 2, 2, 1], [2, 2]))
