# 面向对象
# 有意义的面向对象的代码
# 类=面向对象
# 类,对象
# 实例化
# 类最基本的作用:封装
class Student():
    # 全局变量
    name = '1111'
    age = 0

    # 类变量是和类相关的变量
    # 实例变量
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #      构造函数默认返回值为None
        #     returnn=none
        # print("student")

    def do_homework(self):
        print('homework')

    # 在类下面的函数中必须加入self,self.才能引用类中的全局变量
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


# class StudentHonemwork():
#     homwwork_name=''

# student = Student()
# student.print_file()
student1 = Student('王德法', 18)
student2 = Student('左翼', 20)
print(student2.name)
print(Student.name)
print(student1.name)
