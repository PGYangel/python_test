# 字典
'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''

dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'

tinydict = {'name': 'john', 'code': 123456, 'dept': 'sales'}

print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# 因为字典类型的key是唯一的，后赋值同名key值会覆盖前面的key值
test = {'name': 'john', 'name': 'hong'}
print(test)
# 如果用字典里没有的键访问数据，会输出错误
'''
修改字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
'''
'''
删除字典元素
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空字典所有条目
del dict          # 删除字典
'''
'''
字典键的特性
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
'''
'''
字典内置函数&方法
Python字典包含了以下内置函数：
序号	函数及描述
1	    cmp(dict1, dict2)
        比较两个字典元素。
2	    len(dict)
        计算字典元素个数，即键的总数。
3	    str(dict)
        输出字典可打印的字符串表示。
4	    type(variable)
        返回输入的变量类型，如果变量是字典就返回字典类型。
        
Python字典包含了以下内置方法：
序号	函数及描述
1	    dict.clear()
        删除字典内所有元素
2	    dict.copy()
        返回一个字典的浅复制
3	    dict.fromkeys(seq[, val])
        创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
4	    dict.get(key, default=None)
        返回指定键的值，如果值不在字典中返回default值
5	    dict.has_key(key)
        如果键在字典dict里返回true，否则返回false
6	    dict.items()
        以列表返回可遍历的(键, 值) 元组数组
7	    dict.keys()
        以列表返回一个字典所有的键
8	    dict.setdefault(key, default=None)
        和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	    dict.update(dict2)
        把字典dict2的键/值对更新到dict里
10	    dict.values()
        以列表返回字典中的所有值
11	    pop(key[,default])
        删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	    popitem()
        随机返回并删除字典中的一对键和值。
'''
