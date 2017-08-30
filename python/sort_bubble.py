def swap(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp


def sort_bubble(lst):
    for last_pos in range(len(lst) - 1, 0, -1):
        for i in range(0, last_pos):
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)
    return lst


