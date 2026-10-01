courses = [
    {"name": "高等数学", "credits": 4, "grade": 88},
    {"name": "C语言", "credits": 3, "grade": 92},
    {"name": "大学英语", "credits": 2, "grade": 79},
]
print(courses[0]["name"])
print(courses[1]["credits"])
for i in courses:
    print(f"{i['name']}: {i['credits']}学分, {i['grade']}分")
total = 0
for course in courses:
    total += course["grade"]
print(total)