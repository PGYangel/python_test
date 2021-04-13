#引用re模块来使用正则表达式
import re

a='C|C++|C#|Java|Javascript|Python|asdf4512'

#用python内置函数来检测
print(a.index('Python')>-1)
print('Python' in a)

#使用re模块方法来检测
#re.findall('正则表达式',检测参数)
r=re.findall('Python',a)
print(r)

#\d，查找数字
print(re.findall('\d',a))

b='abc,acc,adc,aec,afc,agc'
#获取中间是c或f的词
print(re.findall('a[cf]c',b))
#不获取中间是c或f的词
print(re.findall('a[^cf]c',b))
#中间连续省略写法
print(re.findall('a[c-f]c',b))
