#Noh Daniel
#2023/10/18
#This is a temperature convertor. It will ask the user for a temperature and unit,
#then convert it to the opposite unit (32F will turn to 0C).

print("Welcome to the temperature convertor! This program will get a temperature from"
      "you, then convert it to the opposite unit.")

temp=float(input("Enter the temperature"))
unit=input("Is it in Fahrenheit (F) or Celsius (C)? ")

if unit == "F":
    ans=(temp - 32) * 5 / 9#Formula for Fahrenheit to Celcius
    print(temp, "Fahrenheit =", ans, "Celsius.")
elif unit == "C":
    ans=(temp * 9 / 5) + 32 #Formula for Celcius to Fahrenheit
    print(temp,"Celcius =", ans, "Fahrenheit.")
else:
    print("I don't understand. Please use 'F' or 'C' for the unit.")