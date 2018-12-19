# 函数定义时可以定义默认参数
# 没有默认值的时候参数，必须传入值
def print_student_files(name,gender='男',age='18',
                        collage='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print("就读于"+collage)

print_student_files('王德法',"男",'18','北京大学')
print_student_files('陈富健')
print_student_files("王",'女')
print_student_files('李',age=20)