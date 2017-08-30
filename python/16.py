# 1.判断101-200之间有多少个素数，并输出所有素数
lst = []
for i in range(100):
    lst.append(101 + i)
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            lst.remove(i)
            break
print(len(lst))
print(lst)

# 2.打印出所有的"水仙花数"
# for n in range(100, 1000):
#     i = int(n / 100)
#     j = int(n / 10) % 10
#     k = n % 10
#     if n == i * i * i + j * j * j + k * k * k:
#         print(n)

# 3.将一个正整数分解质因数

# 4.学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# score = int(input('input score:\n'))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
#
# print('{0} belongs to {1}'.format(score, grade))
# 5.
# lloyd = {
#     "name": "Lloyd",
#     "homework": [90.0, 97.0, 75.0, 92.0],
#     "quizzes": [88.0, 40.0, 94.0],
#     "tests": [75.0, 90.0]
# }
# alice = {
#     "name": "Alice",
#     "homework": [100.0, 92.0, 98.0, 100.0],
#     "quizzes": [82.0, 83.0, 91.0],
#     "tests": [89.0, 97.0]
# }
# tyler = {
#     "name": "Tyler",
#     "homework": [0.0, 87.0, 75.0, 22.0],
#     "quizzes": [0.0, 75.0, 78.0],
#     "tests": [100.0, 100.0]
# }
#
# Add your function below!
# def average(numbers):
#     total = sum(numbers)
#     total = float(total)
#     result = total / len(numbers)
#     return result
# def get_average(student):
#     homework = average(student["homework"])
#     quizzes = average(student["quizzes"])
#     tests = average(student["tests"])
#     return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
# def get_letter_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >=80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
#
# def get_class_average(students):
#     results = []
#     for student in students:
#         get_average(student)
#         results.append(get_average(student))
#     return (average(results))
#