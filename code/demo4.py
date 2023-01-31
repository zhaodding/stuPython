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