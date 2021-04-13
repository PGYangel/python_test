# while语句
num = 1
while num <= 10 :
    print(num)
    num+=1
else:
    print('exit',num)

# for 循环
arr = [[1,2,3],(4,5,6)]
for x in arr:
    for y in x:
        print(y)
else:
    print('exit')
#注意，如果使用break结束循环，不会执行else里面的语句。

# 使用for语句实现传统for循环：for(i=0;i<10;i++)
# range可以生成一个序列
for x in range(0,10):
    print(x)

# 如果想range生成一个偶数序列则加多一个参数range(0,10,2)
for x in range(0,10,2):
    print(x)

# 用range生成一个反序列
for x in range(10,0,-2):
    print(x)

# 练习，打印a=[1,2,3,4,5,6,7,8,9]里面间隔数值
a=[1,2,3,4,5,6,7,8,9]
for x in range(0,len(a),2):
    print(a[x])
# 使用第三个参数偏移量进行截取
b = a[0:len(a):2]
print(b)