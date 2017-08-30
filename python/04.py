def func1(num):
    for i in range(1, num + 1):
        str1 = ""
        for j in range(1, i + 1):
            str2 = str(i) + "*" + str(j) + "=" + str(i * j) + " "
            str1 = str1 + str2
        print(str1)


func1(9)
