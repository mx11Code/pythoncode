# get minimum number of coins to combine to target
coin_set = [2, 5, 7, 11]
min_coin = min(coin_set)
cache = {}


def minimum(target):
    if target in cache:
        return cache[target]
    if target in coin_set:
        return 1
    possible_solution = []
    for picked in coin_set:
        left = target - picked
        if left >= min_coin:
            result = minimum(left)
            if result:
                possible_solution.append(1 + result)
    if len(possible_solution) > 0:
        val = min(possible_solution)
        cache[target] = val
        return val
    else:
        return False

# val = minimum(18)
# print(val)


def loop(target):
    results = [-1 for i in range(target)]
    results[0] = 0
    for i in range(1,target+1):
        results