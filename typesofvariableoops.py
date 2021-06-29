#Static variable
#Instance variable 
#local variable


class Student:
    school_name = "CloudBlitz"  #static variables

    def __init__(self, name, id) -> None:
        self.name = name   #instance variable 
        self.id = id       #instance vaiable 
        print("My name is ", self.name , "and roll number is ", self.id)
        print ("My school is", Student.school_name)

    def information(self):
        x = 10     #local variable 
        for i in range(x):
            print (i)


s1 = Student("Aditya",10)
s2 = Student("Adi",110)
s1.information()