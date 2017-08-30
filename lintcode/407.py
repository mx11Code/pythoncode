def plusOne(digits):
    digits.reverse()
    digits[0] += 1
    for item in digits:
        if item == 10:
            pos_10 = digits.index(10)
            if pos_10 != len(digits) -1:
                digits[pos_10] = 0
                digits[pos_10 + 1] += 1
            elif pos_10 == len(digits) - 1:
                digits[pos_10] = 0
                digits.append(1)

    digits.reverse()
    return digits