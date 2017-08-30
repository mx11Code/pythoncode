def censor(text, word):
    lst = text.split(" ")
    for i in range(0, len(lst)):
        if lst[i] == word:
            lst.pop(i)
            lst.insert(i, "*" * len(word))
    text1 = " ".join(lst)
    return text1


print(censor("this hack is wack hack", "hack"))

