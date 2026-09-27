people = int(input("有几个学生？"))
total = 0
for i in range(1 , people+1):
    score = int(input(f"第{i}个分数:"))
    total += score
result = total/people
print(f"平均分是 {result:.2f}")