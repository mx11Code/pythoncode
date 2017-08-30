def sort_insertion(lst, comparison):
    def func(sorted_list, number):

        for i in range(0, len(sorted_list)):
            # if comparision(number) < comparision(sorted_list[i]):
            if comparison(number, sorted_list[i]):
                sorted_list.insert(i, number)
                return

        sorted_list.append(number)

    list2 = []
    for i in range(0, len(lst)):
        func(list2, lst[i])
    return list2


def comparision_number(a, b):
    return a < b


print(sort_insertion([2, 1, 10, 8, 5], comparision_number))


# class Human:
#     age = None
#     height = None
#
#     def __init__(self, a, h):
#         self.age = a
#         self.height = h
#
#
# def comparision_age(a, b):
#     return a.age < b.age
#
#
# def comparision_h(a, b):
#     return a.height < b.height
#
#
# lc = Human(23, 173)
# mx = Human(24, 176)
# hf = Human(30, 160)
#
# print("lc, mx, hf", lc, mx, hf)
#
# print(sort_insertion([lc, mx, hf], comparision_h))
