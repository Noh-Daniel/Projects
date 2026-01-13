num = 1

while True:
    P_input = input("Input the principal amount. If you would like to exit, input 'exit':   ")

    if P_input == 'exit':
        exit()

    P = int(P_input)

    if P <= 0:
        print("Principal amount is invalid. Please input an amount above 0.")
        continue

    r_input = input("Input the interest rate as a percentage. If you would like to exit, input 'exit':    ")

    if r_input == 'exit':
        exit()

    r = float(r_input)

    if r <= 0:
        print("Interest rate is invalid. Please input an amount above 0.")
        continue

    n_input = input("Input the number of years. If you would like to exit, input 'exit':   ")

    if n_input == 'exit':
        exit()

    n = int(n_input)

    if n <= 0:
        print("Number of years is invalid. Please input an amount above 0.")
        continue

    print('Years:', 'Future Value:')

    def compoundInterest_function(p=P, r=r, n=n):
        for year in range(1, n + 1):
            p = p * (1 + r)  # Update principal for each year
            print(year, p)

        return round(p, 2)

    compoundInterest_function()
