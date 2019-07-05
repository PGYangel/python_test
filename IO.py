'''
Python 文件I/O
本章只讲述所有基本的的I/O函数，更多函数请参考Python标准文档。
'''
'''
打印到屏幕
最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。
此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出如下：

print "Python 是一个非常棒的语言，不是吗？"
'''
'''
读取键盘输入
Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
raw_input
input

raw_input函数
raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
str = raw_input("请输入：")
print "你输入的内容是: ", str
这将提示你输入任意字符串，然后在屏幕上显示相同的字符串。当我输入"Hello Python！"，它的输出如下：
请输入：Hello Python！
你输入的内容是:  Hello Python！

python3.0版本后用input替换了raw_input
str = input("请输入：")
print("你输入的内容是: ", str)

input函数
input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，
但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
str = input("请输入：")
print "你输入的内容是: ", str

这会产生如下的对应着输入的结果：
请输入：[x*5 for x in range(2,10,2)]
你输入的内容是:  [10, 20, 30, 40]
'''
'''
打开和关闭文件
现在，您已经可以向标准输入和输出进行读写。现在，来看看怎么读写实际的数据文件。
Python 提供了必要的函数和方法进行默认情况下的文件基本操作。你可以用 file 对象做大部分的文件操作。

open 函数
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
语法：
file object = open(file_name [, access_mode][, buffering])


'''

