# 闭包是函数加环境变量
def fn():
    a = 25
    def outFn(x):
        return a*x
    return outFn
a=10
f = fn()
print(f(2))
print(f.__closure__) #可以使用__closure__属性来检测是否是闭包