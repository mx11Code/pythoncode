def climbstairs(n):
    fn = [1 for i in range(0, n+1)]
    for i in range(2, n+1):
        fn[i] = fn[i-1] + fn[i-2]
    return fn[n]

def climb_stairs(n):
    fn = [0, 1, 2]
    for i in range(3, n+1):
        fn.append(fn[i-1] + fn[i-2])
    return fn[n]
