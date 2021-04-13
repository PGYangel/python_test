# 给a列表，每一项都做一个平方输出新列表
a = [1,2,3,4,5,6]

b = [i*i for i in a]
print(b) #[1, 4, 9, 16, 25, 36]

# 当数字大于等于5的项才进行平方运算
c = [i*i for i in a if i>=5]
print(c) #[25, 36]

#集合推导式
aa = {1,2,3,4,5,6}
d = {i*i for i in aa if i>=5}
print(d) #{25, 36}

# 元组推导式
aaa = (1,2,3,4,5,6)
e = (i*i for i in aaa if i>=5)
print(e) #<generator object <genexpr> at
# generator对象用for循环遍历
for gen in e:
    print(gen)

#字典推导式
aaaa = {
    '小麦': 18,
    '小红': 12,
    '小黄': 20
}
f = [key for key,value in aaaa.items()]
# 让原来的key,value颠倒
g = {value:key for key,value in aaaa.items()}
print(f) #['小麦', '小红', '小黄']
print(g) #{18: '小麦', 12: '小红', 20: '小黄'}
