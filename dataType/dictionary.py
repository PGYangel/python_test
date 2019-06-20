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
