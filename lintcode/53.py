def reverseWords(s):
    s = s.strip()
    content = s.split(" ")
    content.reverse()
    return " ".join(content)