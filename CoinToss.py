count=int(input("How many times would you like to flip a coin?: "))
for x in range (count):
    import random
    ans = random.randint(1, 2)
    if ans == 1:
            print("Heads")
    elif ans == 2:
            print("Tails")
