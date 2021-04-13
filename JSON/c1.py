import json

#反序列化
str = '{"name":"dabao","age":18}'

student = json.loads(str)
print(student)
print(type(student))

str2 = '[{"name":"dabao","age":18},{"name":"dabao","age":18}]'

student2 = json.loads(str2)
print(student2)
print(type(student2))

str3 = '{"name":"dabao","age":18,"isShow":false}'

student3 = json.loads(str3)
print(student3)
print(type(student3))

#序列化
students = [
    {'name':'liqi','age':18,'flag':False},
    {'name':'liqi','age':18,'flag':False}
]
mjson = json.dumps(students)
print(mjson)
print(type(mjson))