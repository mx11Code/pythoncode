alphabet = "abcdefghijklmnopqrstuvwxyz"

print("input your search:")
word = input()


word_set_extra = []
for l in alphabet:
    tmp = [word[:i] + l + word[i:] for i in range(0, len(word) + 1)]
    word_set_extra.extend(tmp)

word_set_less = [word[:i] + word[i + 1:] for i in range(0, len(word))]

word_set_typo = []
for l in alphabet:
    tmp = [word[:i] + l + word[i + 1:] for i in range(0, len(word))]
    word_set_typo.extend(tmp)

word_set_possible = word_set_extra + word_set_less + word_set_typo


correct_word = ['huangfei', 'luochao', 'pengmengxiong']
candidate = []
for c in correct_word:
    if c in word_set_possible:
        candidate.append(c)

print("are you looking for:", candidate)
