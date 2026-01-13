num=int(input("Give me a positive number"))
num2=int(input("Give me another"))
num3=int(input("One more!"))

if num or num2 or num3 < 0:
    print("Please input a positive number!")
else:
    if num > num2 or num3:
        print(num, "is the greater number")

#if num>num2:
#    print("The greater number is", num)
#else:
#     print("The greater number is", num2)