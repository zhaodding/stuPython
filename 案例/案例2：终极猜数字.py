# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/2/1 20:20 
# @Function    : 终极猜数字

# 1.构建一个随机的数字变量
import random
num = random.randint(1, 10)

guess_num = int(input("输入要猜测的数字："))

# 2.通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("很遗憾，猜的偏大了")
    else:
        print("猜测的数字偏小了")

    guess_num = int(input("请第二次再输入要猜测的数字："))

    if guess_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > num:
            print("很遗憾，猜的偏大了")
        else:
            print("猜测的数字偏小了")

        guess_num = int(input("请第三次再输入要猜测的数字："))

    if guess_num == num:
        print("恭喜，第三次就猜中了")
    else:
        print("很遗憾，三次都没有猜中。")