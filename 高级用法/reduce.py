from functools import reduce

list_x=[1,2,3,4,5,6,7,8]
# reduce的lambda表达式一定是两个参数
r=reduce(lambda x,y:x+y,list_x)
# reduce是连续做计算，这里做的是列表累加
print(r)

