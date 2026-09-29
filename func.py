def calc_avg(a, b, c):
    return (a + b + c) / 3
print(calc_avg(80, 90, 100))
def get_average(n):
    total = 0
    for i in range(1, n + 1):
        score = int(input(f"第{i}个分数: "))
        total += score
    return total / n
count = int(input("有几个学生？ "))
avg = get_average(count)
print(f"平均数是{avg:.2f}")