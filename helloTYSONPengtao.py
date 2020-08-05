class person:
    number=0
    def __init__(self,name,gender,age,):
        self.name=name
        self.gender=gender
        self.age=age
        person.number+=1
    def displayperson(self):
        print("name:",self.name,"gender:",self.gender,"age:",self.age)
    def displaynumber(self):
        print("total person:",person.number)
stul=person("lingling","m",21)
stu2=person("pengtao","h",22)
setattr(stul,"score",90)
setattr(stul,"score",100)
stul.displayperson()
stu2.displayperson()
print("total students:",person.number)
stul.scoure=90
stu2.scoure=100
print(getattr(stul,"score"))
print("the scoure for the first students:",stul.scoure)
delattr(stul,"score")
print(hasattr(stul,"score"))