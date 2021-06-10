a = 20

if  a > 10:
    print ("A is greater than 10")
    if a > 30:
        print ("A is greater than 30")
        if a > 50:
            print ("A is greater than 50")
        else:
            print ("A is less than 50")
    else: 
        print ("A is not greater than 30 and Second condition not satifised")
else: 
    print ("First conditino not satified")