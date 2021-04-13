#对列表字典内容进行排序
a = [
    {'name':'小麦1','age':'18'},
    {'name':'小麦2','age':'10'},
    {'name':'小麦3','age':'1'},
    {'name':'小麦4','age':'20'},
    {'name':'小麦5','age':'28'},
    {'name':'小麦6','age':'10'},
    {'name':'小麦7','age':'9'},
    {'name':'小麦8','age':'55'},
    {'name':'小麦9','age':'44'},
]
def rName(obj):
    result = int(obj['age'])
    return result
sort = sorted(a,key = rName,reverse=False)
for s in sort:
    print(s)
