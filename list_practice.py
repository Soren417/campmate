courses = ["高数", "C语言", "大学英语"]
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
for c in courses:
    print(c)
courses.append("AI导论")
courses.insert(0,"体育")
courses.remove("C语言")
del courses[0]
last = courses.pop()
print(last)
print(courses)