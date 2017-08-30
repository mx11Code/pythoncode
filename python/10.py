def func(p):
    if isinstance(p, list):
        for item in p:
            func(item)
    else:
        print(p)


func([1, 2, [31, [321, 322]]])
