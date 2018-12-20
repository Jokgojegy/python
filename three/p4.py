import re

a = 'pytho0python1pythonn2py3'
#  "*"前的字符可以出现0次或者无限多次
r = re.findall('python*', a)
#  "+"前的字符最少出现一次或这无限多次
s = re.findall('python+', a)
#  “？”前的字符出现1次或者无限多次
t = re.findall('python?', a)

# 贪婪  与  非贪婪
#   贪婪
B = re.findall('python{1,2}', a)
#   非贪婪
b = re.findall('python{1,2}?', a)

print(r)

# 边界匹配
qq = '1000100001'
# ^ 从首字符开始匹配
# $ 从尾字符开始匹配
q = re.findall('^\d{0,10}$', qq)

print(q)
