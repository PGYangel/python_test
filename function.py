'''
函数：
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
1.函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
2.任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
3.函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4.函数内容以冒号起始，并且缩进。
5.return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''
'''
python 传不可变对象实例
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print b # 结果是 2

实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，
按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，
则新生成一个 int 值对象 10，并让 a 指向它。
'''
'''
传可变对象实例
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist

实例中传入函数的和在末尾添加新内容的对象用的是同一个引用，故输出结果如下：
函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
'''
'''
参数
以下是调用函数时可使用的正式参数类型：
必备参数
关键字参数
默认参数
不定长参数
'''
'''
必备参数
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用printme()函数，你必须传入一个参数，不然会出现语法错误：
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
#调用printme函数
printme(); # 此时会报错
'''
'''
关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

以下实例在函数 printme() 调用时使用参数名：
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;

#调用printme函数
printme( str = "My string");
以上实例输出结果：
My string

下例能将关键字参数顺序不重要展示得更清楚：
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );
以上实例输出结果：
Name:  miki
Age  50
'''
