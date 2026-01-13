print(
    "Enter a starting number.\n"
    "Then enter how many operations will follow.\n"
    "For each operation, enter '+' or '-' on one line, followed by a number on the next line.\n"
    "The program will apply each operation and print the final result."
)

d = int(input())
e = int(input())
for i in range(e):
        x = input()
        y = int(input())
        if x == '+':
            d += y
        elif x == '-':
            d -= y
print(d)