from enum import Enum,IntEnum,unique

class VIP(Enum):
    YELLOW = 1
    BLUE = 2
    GREEN = 3
    RED =4

print(VIP.YELLOW)
print(type(VIP.YELLOW))
#获取对应枚举取值
print(VIP.YELLOW.value)
#获取对应枚举标签值
print(VIP.YELLOW.name)
print(type(VIP.YELLOW.name))
'''
如果不用枚举类定义，使用字典或者普通类来定义会有什么问题
1、可变
2、没有防止相同标签的功能
'''
#循环枚举
for v in VIP:
    print(v)

#通过枚举来判断值
a = 2
if VIP(a) == VIP.YELLOW:
    print('这个值与YELLOW对应')
else:
    print('a值与YELLOW不对应')

# 枚举可以定义值相等标签不等，但是第二个标签会是第一个标签的别名
class VIP2(Enum):
    YELLOW = 1
    BLUE =1
    GREEN = 3
    RED = 4
print(VIP2.BLUE) #VIP2.YELLOW
# BLUE不会被打印出来
for v in VIP2:
    print(v)
#如果需要打印别名则使用如下方式
for v in VIP2.__members__:
    print(v)

#只允许是数字枚举使用IntEnum
#不允许值重复使用unique修饰符
@unique
class VIP3(IntEnum):
    YELLOW=1