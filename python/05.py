def make_line(line_num, end):
    str1 = ""
    for j in range(1, line_num+1):
        str1 = str1 + str(line_num) + "*" + str(j) + "=" + str(line_num * j) + " "
    return 3 * (end-line_num) * " " + str1


def main(end):
    for i in range(1, end+1):
        line_str = make_line(i, end)
        print(line_str)


main(8)





























