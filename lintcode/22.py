new_list = []


def flatten(nested_list):
    if isinstance(nested_list, int):
        return [nested_list]
    for i in nested_list:
        if not isinstance(i, list):
            new_list.append(i)
        else:
            flatten(i)
    return new_list
