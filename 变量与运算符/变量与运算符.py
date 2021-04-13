#变量赋值
A = [1,2,3,4]
print(A)

#值类型：int，str，tuple
#引用类型：list，set，dict
#所以python也有深浅拷贝问题

#如果元组里面有可改变的引用类型，里面的引用类型值是可以被改变。
a = (1,2,3,[1,2,4])
a[3][2] = '4'
print(a)

'''
算数运算符：+、-、*、/、//、**、%
赋值运算符：=、+=、-=、*=、/=、%=、**=、//=
关系运算符：==、!=、>、<、>=、<=
逻辑运算符：and、or、not
成员运算符：in、not in
身份运算符：is、is not
位运算符：&、|、^、~、<<、>>
'''

#判断变量类型：isinstance
print(isinstance(a,tuple))
#isinstance第二个参数可以是元组，可以判断是否是其中一个类型
print(isinstance(a,(int,str,tuple)))

#对象三个特征，id，value，type