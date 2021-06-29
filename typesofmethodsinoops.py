#Types of methods
#Instance Method
#Class Method
#Static Method


class Student:

    school = "Cloudblitz"
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id 

    def information(self):                            # instance method
        print(self.name, self.id)
  
    @classmethod  
    def getSchool(cls):
        print(Student.school)
    
    @staticmethod
    def getSum(a,b):
        print (a+b)

s1 = Student("Aditya", 33)
s1.information()
s1.getSchool()
s1.getSum(10,20)
