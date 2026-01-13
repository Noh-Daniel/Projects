print("Input the number of codes, then enter each code. Letters are kept, numbers are added, and numbers after '-' are subtracted.")
#A code is a line of text made up of capital letters, numbers, and optional minus signs that the program reads,
# keeps the letters, and uses the numbers to calculate a final total.

num_codes = int(input())

for i in range(num_codes):
    code = input()
    new_code = ""
    total = 0
    j = 0

    while j < len(code):
        ch = code[j]

        if 'A' <= ch <= 'Z':
            new_code += ch
            j += 1

        elif ch == '-' and j + 1 < len(code) and '0' <= code[j + 1] <= '9':
            j += 1
            number = 0
            while j < len(code) and '0' <= code[j] <= '9':
                number = number * 10 + int(code[j])
                j += 1
            total -= number

        elif '0' <= ch <= '9':
            number = 0
            while j < len(code) and '0' <= code[j] <= '9':
                number = number * 10 + int(code[j])
                j += 1
            total += number

        else:
            j += 1

    print(new_code + str(total))
