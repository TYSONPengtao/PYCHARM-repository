#构造函数
class person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
stu1=person("lingming","m",19)
stu2=person("zhangli","m",21)
print("name:",stu1.name,"gender:",stu1.gender,"age:",stu1.age)
print("name:",stu2.name,"gender:",stu2.gender,"age:",stu2.age)