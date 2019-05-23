country = input("请输入你的国家：")
age = int(input("请输入你的年龄："))
if country == "中国":
    if age >= 18:
        print("你可以考驾照")
    else:
        print("你不可以考驾照")