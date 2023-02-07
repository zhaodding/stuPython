# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/2/1 19:37 
# @Function    : 猜猜心里数字

print('----------- if-else ------------')

# 定义一个变量数字
num = 5
if int(input("请输入一个数字：")) == num:
     print("恭喜第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
if int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次，猜对了")
else:
    print("Sorry，猜错了")

print('----------- while ------------')
# 设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
# 无限次机会，直到猜中为止
# 每一次猜不中，会提示大了或小了
# 猜完数字，提示猜了几次

# 获取范围1-100的随机数字
import random
num = random.randint(1, 100)
# 定义一个变量，记录总共猜测的次数
count = 0

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入猜测的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 设置false就是终止的条件
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
print(f"总共猜测了{count}次")
