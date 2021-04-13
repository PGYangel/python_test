list_x=[1,2,3,4,5,6,7,8]

def squery(x):
    return x*x

#使用map映射循环执行squery，输出新的map对象列表
r = map(squery,list_x)
print(r)
print(list(r))

#使用lambda表达式来实现
r1 = map(lambda x:x*x,list_x)
print(list(r1))

list_y=[1,2,3,4,5,6,7,8]
r2 = map(lambda x,y:x+y,list_x,list_y)
print(list(r2))