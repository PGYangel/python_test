# 布尔类型归为Number数字类型
# 布尔类型True和False都需要大写，开头不能用小写

# 为什么会归为数字类型，因为可以使用int方法将他转换为数字，bool方法可以将数字转换为True,False
print(int(True))
print(int(False))

#非0数字都表示True，只有0表示False
print(bool(1.1))
print(bool(-1.1))
print(bool(0))
print(bool(0b0))

#其他数据类型，如果是空也会表示为False
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(None))