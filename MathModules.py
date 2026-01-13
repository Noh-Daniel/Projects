#import math
#num=int(input("Enter a value:"))

#print("The absolute value is:", math.fabs(num))
#print("The square root is:", math.sqrt(num))
#^^^Does not work if negative. Change to absolute value to work^^^
#print("The quartic value is:", math.pow(num, 4))
#--------------------------------------------------
#How to fix
import math
num=int(input("Enter a value:"))
pos=math.fabs(num)
print("The absolute value is:", math.fabs(num))
print("The square root is:", math.sqrt(pos))
print("The quartic value is:", math.pow(num, 4))