class Student:
    school = "TINTY"
    def __init__(self) -> None:
        self.name = "aditya"
        print (self.name)
        print(Student.school)
    
    def name2(self) ->None:
        print(self.name)


c1 = Student()
c1.name2()
c2 = Student()