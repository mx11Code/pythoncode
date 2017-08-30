def searchInsert(A, target):
    def insert(sorted_list, number):
        for i in range(len(sorted_list)):
            if number <= sorted_list[i]:
                sorted_list.insert(i, number)
                return
        sorted_list.append(number)

    if target in A:
        return A.index(target)
    else:
        insert(A, target)
        return A.index(target)
