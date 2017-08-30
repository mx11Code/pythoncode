def func(target):
    coins = [2, 3, 5, 7]
    fn = [0]
    for i in range(1, target + 1):
        solution = []
        for picked in coins:
            left = i - picked
            if left >= 0 and fn[left] != "x":
                solution.append(1 + fn[left])
        if solution:
            fn.append(min(solution))
        else:
            fn.append("x")
    return fn[target]


print(func(11))


def func2(target):
    coins = [2, 3, 5, 7]
    if target == 0:
        return 0
    solutions = []
    for picked in coins:
        left = target - picked
        if left >= 0:
            best_of_left = func2(left)
            if best_of_left != 'x':
                solutions.append(1 + func2(left))
    return min(solutions) if solutions else 'x'


print(func2(11))
