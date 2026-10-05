import json
import os

DATA_FILE = "my_courses.json"

def show_courses(courses):
    """打印课表"""
    if len(courses) == 0:
        print("课表是空的")
        return

    print(f"📚 当前课表（共 {len(courses)} 门）：")
    for i, c in enumerate(courses, 1):
           grade = c.get("grade", "未录入")
           print(f"  {i}. {c['name']} —— {c['credits']} 学分，{grade} 分") 

def save_courses(courses):
    """保存课表到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)


if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f :
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
        show_courses(courses)

    if choice == "2":
        name = input("课程名称：")
        credit = int(input("学分："))
        grade = int(input("成绩："))

        courses.append({"name": name, "credits": credit, "grade": grade})
        save_courses(courses)
        print(f"✅ 已添加：{name}  {credit} 学分）")
    
    if choice == "3":
        if len(courses) == 0:
            print("课表是空的，没有可删的课")
        else:
           show_courses(courses)
           num = int(input("请输入要删除的编号："))
           if 1 <= num <= len(courses):
                removed = courses.pop(num - 1)
                print(f"🗑️ 已删除：{removed['name']}")
                save_courses(courses)
                
           else:
                print("❌ 编号不存在") 