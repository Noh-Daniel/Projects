#Noh Daniel
#2023/10/18
#This is a mini calculator that will add, subtract, multiply, or divide
#the first number by the second.

print("Welcome to your very own personal mini calculator! Enter any two numbers, "
      "then what you want to do to them. Follow the operators as shown. Enjoy!")

int1=float(input("Enter an integer"))
int2=float(input("Enter another"))
operator=input("Do you want to +,-,/,* the number? Use the same operators as shown!")
#If the correct operator is not used, the program will stop.

if operator == "+":
    print(int1,"+",int2)
    print(int1+int2)
elif operator == "-":
    print(int1,"-",int2)
    print(int1-int2)
elif operator == "*":
    print(int1,"*",int2)
    print(int1*int2)
elif operator == ("/"):
    print(int1,"/",int2)
    print(int1/int2)
