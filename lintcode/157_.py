def isUnique(s):
    # write your code here
    ch = range(129)
    for i in range(129):
        ch[i] = 0
    for i in range(len(s)):
        if ch[ord(s[i])] == 0:
            ch[ord(s[i])] = 1
        else:
            return False
    return True