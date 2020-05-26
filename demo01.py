"""
演示代码回滚操作
"""
import time

s_num = 0
num = 1
while num <= 10:
    """求1-10之间的整数和"""
    s_num += num
    num += 1
    time.sleep(1)

print(f"1-10z之间的整数和是{s_num}")

print("dev2分支下的world")



