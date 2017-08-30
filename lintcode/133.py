def longestWords(dictionary):
    string = ""
    lst_string = []
    for keys in dictionary:
        if len(keys) >= len(string):
            string = keys
    for keys in dictionary:
        if len(keys) == len(string):
            lst_string.append(keys)
    return lst_string