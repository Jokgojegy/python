from two.p5 import People


class Student(People):
    # sum = 0

    def __init__(self, shool, name, age):
        # self.name = name
        # self.age = age
        # People.__init__(self, name, age)
        super(Student, self).__init__(name, age)
        self.shool = shool
        self.__score = 0
        self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')


student1 = Student('人民路小学', '石敢当', 20)
student1.do_homework()
# print(Student.sum)
# print(student1.sum)
print(student1.name)
print(student1.age)
# student1.get_name()
