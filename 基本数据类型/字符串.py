# 字符串表示方式，单引号，双引号，三引号

#字符串转义字符\
print('hjkh\'kjlk')

# 三引号解决字符串过长换行问题
print('''见都洒了看风景
爱神的箭反馈j
sdfdf ''')

#单双引号也能换行，加\即可
print('asdjlfk\
kjlasdf')
# 如何输入无需转义的字符串\n
print('hello \n world')
print('hello \\n world')
print(r'hello \n world') # 字符串前面加上r，就不是普通字符串，而是原始字符串

#字符串重复N次，使用*
print('hello'*3)

#获取字符串其中某些字符
print('hello'[0]) #h
print('hello'[-1]) #o
print('hello world'[0:5]) #hello
print('hello world'[0:-1]) #hello worl
print('hello world'[6:]) #world
print('hello world'[-5:]) #world
print('hello world'[:5]) #hello