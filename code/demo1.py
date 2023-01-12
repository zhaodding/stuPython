# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/10/9 7:47
# @Function    : print()函数的使用

# 输出字符串
print(520)
print(98.5)

# 可以输出字符串
print('hello')
print("world")

# 输出含有运算符的表达式
print(3 + 1)

# 将数据输出文件中
fp = open('D:/text.txt', 'a+')
print('hello world', file=fp)
fp.close()

# 不进行换行输出
print('hello', 'world', 'python')
