class Student:
    name = ""
    id = 1
    # 类方法
    @classmethod
    def puls_sum(cls,id):
        cls.id +=1
        print(cls.id)
        cls.add(2,9)
        print(id)
    # 静态方法
    @staticmethod
    def add(x,y):
        print("This is static method")
        print(x)
Student.puls_sum(5)
student = Student
Student.add(10,20)