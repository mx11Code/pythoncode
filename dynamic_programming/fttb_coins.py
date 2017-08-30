cache = {}


def minimum_number_coins(target, coin_set=(2, 3, 5, 7)):
    if target in cache:
        return cache[target]
    if target == 0:
        return 0

    possible = []
    for picked in coin_set:
        required = target - picked
        if required >= min(coin_set):
            possible.append(1 + minimum_number_coins(required, coin_set))
        elif required == 0:
            possible.append(1)
    minimum = min(possible)
    cache[target] = minimum
    print("target %d, minimum %d" % (target, minimum))

    return minimum