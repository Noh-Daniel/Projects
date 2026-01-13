# Noh Daniel
# 23/11/30
# This program is a compound interest calculator (A=P(1+r)) that will take a user input and determine
# the future value of investments or loans

num = 1  # Counter for printing years in a loop using the input of n.

while True:
    # User input for the principal amount, with an option to exit.
    P = input("Input the principal amount. If you would like to exit, input 'exit':   ")

    if P == 'exit':  # Check if the user wants to exit.
        exit()

    P = float(P)  # Convert the input into a decimal.
    round(P,2)

    if P <= 0:
        print("Principal amount is invalid. Please input an amount above 0.")
        continue  # Skip to the next part of loop if the principal amount is invalid.

    # User input for the interest rate as a percentage, with an option to exit.
    r = input("Input the interest rate as a percentage. If you would like to exit, input 'exit':    ")

    if r == 'exit':
        exit()

    r = float(r)  # Convert the input into a floating-point number.

    if r <= 0:
        print("Interest rate is invalid. Please input an amount above 0.")
        continue  # Skip to the next iteration if the interest rate is invalid.

    # User input for the number of years, with an option to exit.
    n = input("Input the number of years. If you would like to exit, input 'exit':   ")

    if n == 'exit':
        exit()

    n = int(n)

    if n <= 0:
        print("Number of years is invalid. Please input an amount above 0.")
        continue  # Skip to the next iteration if the number of years is invalid.

    print("\nYears:     Future Value:")

    def compoundInterest_function(p=P, r=r, n=n):
        # Calculate compound interest and print results for each year.
        for x in range(1, n + 1):
            p = p * (1 + r)  # Update principal for each year
            print(x, "        ", p)

        return round(p, 2)

    compoundInterest_function()
