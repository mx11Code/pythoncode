a = ["a", "b", "c", "d"]
b = [x.upper() for x in a]
print(a)
print(b)

a = [0, "a", "b", "c", "d", 1, 2, 3]
b = [x.upper() for x in a if isinstance(x, str)]
print(a)
print(b)
