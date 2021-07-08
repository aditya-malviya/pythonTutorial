#Variable Length argument

#Here we can define a function where no of variable argument are not fixed.

def add (a,*b):
    print (a)
    print (b)  # (4,6)
    c = a
    for i in b:
        c = c + i        #3+6, c =9, 9+6
    print (c)
  #  print (a+b)


add(3,4,6)