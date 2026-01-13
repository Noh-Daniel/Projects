print(
    "Enter the required amount.\n"
    "Then enter the number of items and the value of each item.\n"
    "The program will check if the total value is enough and print 'yes' or 'no'."
)


n=int(input())
c=int(input())
p=int(input())

if (c*p)<n:
    print("no")
if (c*p)>n or c*p==n:
    print("yes")
