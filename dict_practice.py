credits = {"高数": 4, "C语言": 3, "大学英语": 2}
credits["体育"] = 1
credits["高数"] = 5
del credits["C语言"]
print(credits)
print("大学英语" in credits)
for k in credits:
    print(k)
for v in credits.values():
    print(v)
for k, v in credits.items():
    print(f"{k}: {v} 学分")
