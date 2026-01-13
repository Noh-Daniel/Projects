#Noh Daniel
#2023/10/18
#This code will ask for someone's grade out of 100,
#and give them a corresponding letter grade. It will not accept grades above
#100 and below 0

print("Welcome to the grade convertor! This program will get your mark out of 100,"
      "and tell you the corresponding letter grade!")

grade=int(input("What is your grade out of 100"))

if grade>=90 and grade<101:
    print("A+")
elif grade>=80 and grade<90:
    print("A")
elif grade>=70 and grade<80:
    print("B")
elif grade>=60 and grade<70:
    print("C")
elif grade>=50 and grade<60:
    print("D")
elif grade<50 and grade>0:
    print("F")
else:
    print("Invalid grade")

