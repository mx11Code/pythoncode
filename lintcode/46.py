# def majorityNumber(nums):
#     lst = []
#     for i in nums:
#         if i not in lst:
#             count = nums.count(i)
#             if count > (len(nums) // 2):
#                 return i


def majorityNumber(nums):
    counter = {}
    for item in nums:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    for item in counter:
        if counter[item] > (len(nums) // 2):
            return item



