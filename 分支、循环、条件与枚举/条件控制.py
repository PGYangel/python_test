#if语句
check = False
if check:
    print('is True')
else:
    print('is False')

elNum = 2
if elNum == 1:
    print('输出的是1')
elif elNum == 2:
    print('输出的是2')
else:
    print('输出的是其他')

#模拟登陆
name = 'abc'
password = '123'

print('请输入用户名')
user_name = input()
print('请输入密码')
user_password = input()

if user_name == name and user_password == password:
    print('登陆成功')
else:
    print('用户名或密码错误')

#python没有switch语法
