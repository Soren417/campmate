import json
import os

DATA_FILE = "my_courses.json"

def score_to_gpa(score):
    """把百分制分数换算成5分制绩点"""
    if score < 60:
        return 0
    return (score - 50) / 10

def calc_gpa(courses):
    """算加权平均学分绩点（GPA）"""
    total_points = 0
    total_credits = 0
    for c in courses:
        grade = c.get("grade")
        if grade is not None:
            point = score_to_gpa(grade)
            total_points += point * c["credits"]
            total_credits += c["credits"]
    if total_credits == 0:
            return 0
    return total_points / total_credits

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

while True:
    print("===== 我的课表 =====")
    print("  1. 查看课表")
    print("  2. 添加课程")
    print("  3. 删除课程")
    print("  4. 查看GPA")
    print("  5. 退出")
    choice = input("请选择(1-5):")

    if choice == "5":
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

    if choice == "4":
        gpa = calc_gpa(courses)
        print(f"📊 当前 GPA: {gpa:.2f}")
