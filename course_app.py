import json
import os

if os.path.exists("my_courses.json"):
    with open("my_courses.json", "r", encoding="utf-8") as f :
        courses = json.load(f)

else:
    courses = []

print("读到的数据：", courses)
print("课程数量：", len(courses))

while True:
    print("===== 我的课表 =====")
    print("  1. 查看课表")
    print("  2. 添加课程")
    print("  3. 删除课程")
    print("  4. 退出")
    choice = input("请选择(1-4):")

    if choice == "4":
        print("再见！")
        break
    if choice == "1":
        if len(courses) == 0:
            print("课表是空的，去添加几门课吧")
        else:
            print(f"📚 当前课表（共 {len(courses)} 门）：")
            for i, c in enumerate(courses, 1):
                print(f"  {i}. {c['name']} —— {c['credits']} 学分")
    if choice == "2":
        name = input("课程名称：")
        credit = int(input("学分："))

        courses.append({"name": name, "credits": credit})

        with open("my_courses.josn", "w", encoding="utf-8") as f:
            json.dump(courses, f, ensure_ascii=False, indent=4)

        print(f"✅ 已添加：{name}（{credit} 学分）")
    if choice == "3":
        if len(courses) == 0:
            print("课表是空的，没有可删的课")
        else:
            print("📚 当前课表：")
            for i, c in enumerate(courses, 1):
                print(f"  {i}. {c['name']} —— {c['credits']} 学分")

            num = int(input("请输入要删除的编号："))

            if 1 <= num <= len(courses):
                removed = courses.pop(num - 1)
                print(f"🗑️ 已删除：{removed['name']}")

                with open("my_courses.json", "w", encoding="utf-8") as f:
                    json.dump(courses, f, ensure_ascii=False, indent=4)
            else:
                print("❌ 编号不存在")