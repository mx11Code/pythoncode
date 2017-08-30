def func(p):
    if isinstance(p, list):
        for item in p:
            func(item)
    else:
        print(p)


results = []


def flatten(lists):
    for numbers in lists:
        if not isinstance(numbers, list):
            results.append(numbers)
        else:
            flatten(numbers)
    return results
