import re

a = 'c0c++7java9python2javaScript8'
# 'Python' 普通字符 '\d'元字符
r = re.findall('\d', a)
R = re.findall('\D', a)
print(r)
print(R)
