# 列表

#列表截取可接受第三个参数，作用是截取步长

l=['a','b','c','d','e','f','g','h','i','j']
r=['1','2']
print(l)
print(l[1:5])
print(l[1:5:2]) #截取步长为2

# 加号 + 是列表连接运算符，星号 * 是重复操作
print(l*2)
print(l+r)
'''
更新列表
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
'''
'''
删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000]
del list1[2]
'''
'''
Python列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：
Python 表达式	                结果	                        描述
len([1, 2, 3])	                3	                            长度
[1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	            组合
['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	                True	                        元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	                        迭代
'''
'''
Python列表截取
>>>L = ['Google', 'Runoob', 'Taobao']
>>> L[2]
'Taobao'
>>> L[-2]
'Runoob'
>>> L[1:]
['Runoob', 'Taobao']
>>>
Python 表达式	结果	                描述
L[2]	        'Taobao'	            读取列表中第三个元素
L[-2]	        'Runoob'	            读取列表中倒数第二个元素
L[1:]	        ['Runoob', 'Taobao']	从第二个元素开始截取列表
'''
'''
Python列表函数&方法
Python包含以下函数:
序号	函数
1	    cmp(list1, list2)
        比较两个列表的元素
2	    len(list)
        列表元素个数
3	    max(list)
        返回列表元素最大值
4	    min(list)
        返回列表元素最小值
5	    list(seq)
        将元组转换为列表

Python包含以下方法:
序号	方法
1	    list.append(obj)
        在列表末尾添加新的对象
2	    list.count(obj)
        统计某个元素在列表中出现的次数
3	    list.extend(seq)
        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	    list.index(obj)
        从列表中找出某个值第一个匹配项的索引位置
5	    list.insert(index, obj)
        将对象插入列表
6	    list.pop([index=-1])
        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	    list.remove(obj)
        移除列表中某个值的第一个匹配项
8	    list.reverse()
        反向列表中元素
9	    list.sort(cmp=None, key=None, reverse=False)
        对原列表进行排序
'''
