import json
courses = ["高数", "C语言", "大学英语"]
text = json.dumps(courses, ensure_ascii=False)
print(text)
course = {"name": "高等数学", "credits": 4, "grade": 88}
text1 = json.dumps(course, ensure_ascii=False)
print(text1)
print(type(["高数", "C语言"]))
print(type('["高数", "C语言"]'))
raw = '["高等数学", "C语言", "大学英语"]'
result = json.loads(raw)
print(result)
print(type(result))
print(result[0])
courses = [
    {"name": "高等数学", "credits": 4, "grade": 88},
    {"name": "C语言", "credits": 3, "grade": 92},
]
with open("courses.json", "w", encoding="utf-8" ) as f:
    json.dump(courses, f, ensure_ascii=False, indent=4)

with open("courses.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print(loaded[0]["name"])
print(len(loaded))