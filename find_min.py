def findmin(x, y, z):
    minimum=min(x, y, z)
    return minimum
while True:
    con=input("Would you like to continue?")
    if con!="no":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        z = int(input("Enter your third number: "))
        minimum=findmin(x, y, z)
        print(minimum)
