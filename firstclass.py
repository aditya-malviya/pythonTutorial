class Fan:
    def __init__(self, blades, color):
        print(id (self))
        self.blades =  blades
        self.color = color
        print (self.blades)
        print (self.color)
       

firstFan = Fan(3, "Red")
print(id (firstFan))
secondFan = Fan(4, "Black")
print(id (secondFan))