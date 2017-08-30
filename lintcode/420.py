def countAndSay(n):
    # Write your code here
    i = 1
    count = 1
    newS = "1"

    while i < n:
        s = newS
        newS = ""

        for j in range(len(s)):
            if (j + 1) < len(s) and s[j] == s[j + 1]:
                count += 1
            else:
                newS = newS + str(count) + s[j]
                count = 1
        i += 1
    return newS
