# python的数字类型只有int和float两种，没有双精度，float就是双精度类型。
print(type(1)) # int
print(type(1.1)) # float

# 加法、乘法、减法，int和float组合都会成为float类型，只有int和int组合才会出来int类型
print(type(1+1)) #int
print(type(1+1.1)) #float
print(type(1-1)) #int
print(type(1.1-1)) #float
print(type(1*1)) #int
print(type(1*1.0)) #float

# 除法如果int除以int，那么是float，要想使结果为int则使用//运算
# 原因是/是除法，//是整除取整数位内容。
print(type(1/1)) #float
print(type(1//1)) #int
