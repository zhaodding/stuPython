# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/8/15 23:00
# @Function    :  列表

# 创建一个包含数字和字符串的列表
my_list = [1, 2, "three", 4, "five"]

# 打印列表
print(my_list)
print(len(my_list))
print(my_list[len(my_list) - 1])
print(my_list[-1])
print(my_list[0:3])
print(my_list[3:6])
print(my_list[:3])
print(my_list[3:])
print(my_list[:])
print(my_list[0:6:2])

# 访问列表中的元素
print(my_list[2])  # 输出 "three"

# 修改列表中的元素
my_list[1] = "two"
print(my_list)

# 添加元素到列表末尾
my_list.append("six")
print(my_list)

# 从列表中删除元素
my_list.remove("three")
print(my_list)
