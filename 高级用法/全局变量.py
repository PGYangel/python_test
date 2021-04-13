#python的全局变量使用和其他语言不相同，=号左边会认为是定义局部变量，并不会向上作用域找已定义的全局变量
orgin = 0
def fn(x):
    global orgin
    newNum = orgin + x
    orgin = newNum
    return newNum

print(fn(2))
print(fn(5))
print(fn(7))

#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
def outer():
    num = 10
    def inner():
        # nonlocal关键字声明
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()