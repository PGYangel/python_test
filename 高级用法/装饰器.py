import time

# decorator装饰器
def decorator(func):
    # *args可变参数
    # **kw关键字阐述
    def wapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wapper
# 用@符号语法糖调用装饰器
@decorator
def f1(fname):
    print('f1'+fname)

@decorator
def f2(fname,fage):
    print('f2'+ fname + fage)

@decorator
def f3(fname,fage,**kw):
    print('f3'+ fname + fage)
    print(kw)
# 使用@语法糖后，调用不需要跟原来一样那么复杂，不改变原来调用f1的方式
f1(' name')
f2(' name', ' age')
f3(' name', ' age', a=1,b=2,c='123')
# f = decorator(f1)
# f()