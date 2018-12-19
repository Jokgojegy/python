class StudentScore:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 100
        self.__class__.sum += 1

    def marking(self, name, score1):
        if score1 < 0:
            return '请输入正确的学生成绩'
        else:
            self.score = score1
            print(name + '同学本次的考试成绩' + str(self.score))


student = StudentScore()
print(student.marking('石敢当',99))
