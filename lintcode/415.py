import string


def isPalindrome(s):
    new_s = ""
    for char in s:
        if char in string.ascii_letters or char in string.digits:
            new_s += char
    new_s = new_s.lower()
    if new_s == new_s[::-1]:
        return True
    else:
        return False

