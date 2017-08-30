# 写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。
# 给出 s = "abcd"，t="dcab"，返回 true.
# 给出 s = "ab", t = "ab", 返回 true.
# 给出 s = "ab", t = "ac", 返回 false.


def anagram(s, t):
    new_s = [i for i in s]
    new_t = [i for i in t]
    new_s.sort()
    new_t.sort()
    return new_s == new_t
