# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/1/15 22:24 
# @Function    : 3、Python判断语句

if 520 > 250:
    print("520比250大")
else:
    print("ll")

print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9))

print("2 * 3的结果是：%d" % (2 * 3))
print(f"3 * 4的结果是：{3 * 4}")
print("字符串在Python中的类型是：%s" % type('字符串'))

print('----------- 3.1 布尔类型和比较运算符 ------------')
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型数：{type(bool_1)}")
print(f"bool_1变量的内容是：{bool_2}，类型数：{type(bool_2)}")

# 比较运算符的使用
num1 = 10
num2 = 10
print(f"10 == 10的结果数：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的结果数：{num1 != num2}")

num1 = "bytedance"
num2 = "bytedance2"
print(f"bytedance == bytedances 的结果是：{num1 == num2}")

# 大于小于，大于等于，小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5的结果数：{num1 > num2}")
print(f"10 < 5的结果数：{num1 < num2}")

num1 = 10
num2 = 10
print(f"10 >= 10的结果数：{num1 >= num2}")
print(f"10 <= 10的结果数：{num1 <= num2}")

print('----------- 3.2 if 语句的基本格式应用 ------------')
age = 3
if age >= 18:
    print("已经成年")
    print("可以进入社会")
print("结束人生！")

print('----------- 3.3 if-else 语句的基本格式应用 ------------')
age = int(input("请输入你的年龄："))
if age >= 19:
    print("已成年，需要买票10元。")
else:
    print("未成年，可以免费游玩")

print('----------- 3.4 if-elif-else 语句的基本格式应用 ------------')
age = int(input("请输入你的年龄："))
height = int(input("请输入你的体重："))
if age > 18:
    print("已成年，需要买票10元。")
elif height > 180:
    print("体重超标，需要另外加15元。")
else:
    print("未成年，可以免费游玩")

# 方式二：
if int(input("请输入你的年龄：")) > 18:
    print("已成年，需要买票10元。")
elif int(input("请输入你的体重：")) > 180:
    print("体重超标，需要另外加15元。")
else:
    print("未成年，可以免费游玩")

print('----------- 3.5 判断语句的嵌套 ------------')
print("欢迎进入莫克科技有限公司")
if int(input("输入期望工资是多少：")) > 120:
    print("你的期望工资大于120，不满足期望工资")
    print("不过如果你的英语等级四级，可以破格录取")

    if int(input("请输入你的英语等级：")) > 3:
        print("恭喜已经录取，欢迎加入。")
    else:
        print("Sorry，需要考取四级证书")
else:
    print("欢迎加入，开始新的未来！")

print(' ------------ ')

age = 20
year = 3
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄超标了")
        if year > 2:
            print("恭喜，年龄和入职时间符合，可以领取礼物")
        elif level >3:
            print("恭喜，年龄和级别符合，可以领取礼物")
        else:
            print("很遗憾，尽管年龄符合，但入职时间和级别不满足。")
    else:
        print("年龄太大，不符合要求")
else:
    print("年龄不符合要求，很遗憾")