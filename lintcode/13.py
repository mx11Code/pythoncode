def strStr(source, target):
    # write your code here
    if target == None or source == None:
        return -1
    return source.find(target)
