with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("我的第一行数据\n")
with open("abc.txt", "w", encoding="utf-8") as f:
    f.write("苹果\n")
    f.write("香蕉\n")
    f.write("橘子\n")
with open("abc.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"读到：{line.strip()}")
with open("abc.txt", "a", encoding="utf-8") as f:
    f.write("葡萄\n")
with open("abc.txt", "r", encoding="utf-8") as f:
    print("--- 追加之后再读 ---")
    for line in f:
        print(f"读到：{line.strip()}")

