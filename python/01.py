arr = range(101)
sum1 = 0
sum2 = 0
for i in arr:
    print(i)
    if i % 3 == 0 or "3" in str(i):
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
print(sum1, sum2+sum1)



# 检查 arr 是否为空，如果为空则跳出循环否则进入下一步
# 拿出当前值赋值给 i ，若没有当前值跳出循环
# 进入循环体,如果碰到 continue 跳到第一步，如果碰到 break 跳出循环体
# 跳回第一步
