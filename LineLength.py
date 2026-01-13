import math
def lengthOfALine(x1, y1, x2, y2):
    length=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return length
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

lineLength=lengthOfALine(x1,y1,x2,y2)
print(lineLength)