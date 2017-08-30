def replaceBlank(string, length):
    if string is None:
        return length
    lst = []
    for char in string:
        lst.append(char)
    while " " in lst:
        place = lst.index(" ")
        lst.remove(" ")
        lst.insert(place, "%20")
    new_string = "".join(lst)
    return len(new_string)