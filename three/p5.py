# 反序列化
# JSON                Python
# object              dict
# array               list
# string              str
# number              int
# number              float
# true                True
# false               False
# null                None


import json

# JSON object array
json_str = '{"name":"qiyue","age":18}'
json_str1 = '[{"name":"qiyue","age":18},{"name":"qiyue","age":18}]'
# dict
student = json.loads(json_str)

student1 = student['name']
print(type(student))
print(student)
