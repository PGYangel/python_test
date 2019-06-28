# Number(数字)
# 数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
num = 1
print(num)

'''
del语句的语法是
del var1[,var2[,var3[....,varN]]]]
您可以通过使用del语句删除单个或多个对象的引用。例如：
del var
del var_a, var_b
'''
'''
Python 支持四种不同的数值类型：
整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

注意：python不支持long类型
'''
'''
Python math 模块、cmath 模块
Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
Python math 模块提供了许多对浮点数的数学运算函数。
Python cmath 模块包含了一些用于复数运算的函数。
cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
要使用 math 或 cmath 函数必须先导入：
import math
import cmath
'''
'''
Python数学函数
函数	        返回值 ( 描述 )
abs(x)	        返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	    如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	    x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	        返回数字x的平方根
'''
'''
Python随机数函数
函数	                            描述
choice(seq)	                        从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	                        随机生成下一个实数，它在[0,1)范围内。
seed([x])	                        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	                    将序列的所有元素随机排序
uniform(x, y)	                    随机生成下一个实数，它在[x,y]范围内。
'''
'''
Python三角函数
函数	    描述
acos(x)	    返回x的反余弦弧度值。
asin(x)	    返回x的反正弦弧度值。
atan(x)	    返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	    返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	    返回的x弧度的正弦值。
tan(x)	    返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''
'''
Python数学常量
常量	描述
pi	    数学常量 pi（圆周率，一般以π来表示）
e	    数学常量 e，e即自然常数（自然常数）。
'''
