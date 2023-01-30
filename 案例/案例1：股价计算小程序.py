# @Organization: 上海莫克信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/1/28 14:40 
# @Function    : 股价计算小程序

# 定义需要的变量
name = "莫克科技"
stock_price = 19.99
stock_code = "003032"

# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数：%f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))
