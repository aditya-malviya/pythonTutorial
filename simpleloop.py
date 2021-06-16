weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#for in loop
for aditya in weekdays:                         # x = monday, x=tuesday, x=sunday
    print (aditya)


for me in "aditya":
    print (me)

#RANGE

for x in range(101):
    print (x)

for v in range(7,12):
    print (v)


for i in range(2,15,2):
    print (i)



Months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct']
for p in Months:
    if p == 'Feb':
        break
    print (p)

for t in Months:
    if t == 'May':
        continue
    print (t)

for g in [3,4,5,6]:
    pass