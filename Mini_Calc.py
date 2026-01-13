def menuOption1():
    print(a+b)
def menuOption2():
    print(a-b)
def menuOption3():
    print(a/b)
def menuOption4():
    print(a*b)
def menuOption5():
    print(a**b)
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

op=input("Welcome to your mini calculator! There are 5 different menus for you to pick from!"
      "\nMenu1 is adding,\nMenu2 is subtracting, \nMenu3 is dividing \nMenu4 is multiplying,"
      "and \nMenu5 is exponents. \nType which one you want to do!")
if op=="Menu1":
    menuOption1()
