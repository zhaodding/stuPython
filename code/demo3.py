# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/1/12 19:53 
# @Function    : 字符串格式化

print('-----------字符串拼接------------')

name = "上海"
message = "上海莫克科技有限公司，地址在：%s" % name
print(message)

print('-----------对表达式进行字符串格式化------------')
print("1 * 3的结果数：%d" % (1 * 3))
print(f"1 * 2的结果数：{1 * 2}")
print("字符串在Python中的类型名数：%s" % type("字符串"))

print('-----------input语句（函数）------------')
print("请输入姓名：")
name = input()
print("输入的信息数：%s" % name)

# 输入数字类型
num = input("请输入银行卡密码：")
# 数据类型转换
num = int(num)
print("银行卡类型是：", type(num))