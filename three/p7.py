from enum import Enum


class VIP(Enum):
    Yellow = 1
    # YELLOW_ALIAS是YELLOW的别名
    Yellow_ALIAS = 1
    Green = 2
    Black = 3
    Red = 4


# 遍历枚举
for v in VIP:
    print(v)

# 内置的对象别名的遍历(元组类型)
for v in VIP.__members__.items():
    print(v)

# 等值比较
result = VIP.Yellow == VIP.Yellow_ALIAS
print(result)

# 打印枚举的响应的值
print(VIP.Yellow.name)
print(VIP.Yellow)
print(VIP['Green'].name)
