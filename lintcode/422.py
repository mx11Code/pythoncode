def lengthOfLastWord(s):
    s = s.strip()
    lst = s.split(" ")
    lst.reverse()
    return len(lst[0])