def average(a = 9, b = 12):
    print("The average is: ", (a+b)/2)

average(5)    

def name(fname, mname = "Bablu", lname = "Kumar"):
    print("Hello", fname, mname, lname)

name("Mr.", lname = "Prajapati")    

def average(a=9 , b =1):
    print("The average is: ", (a+b)/2)

average(b=9)

average(b=9, a=21)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/ len(numbers))


average(5, 6, 7, 8)        

def name(**name):
    print(type(name))
    print("Hello,",name["fname"], name["mname"], name["lname"])

name(fname = "Mr.", mname = "Bablu", lname = "Prajapati")    