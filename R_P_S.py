player1_score = 0
player2_score = 0
print("This is a rock paper scissors game. Enter R for rock, P for paper, or S for Scissors.")
while True:
    player1_choice = input("Player 1, enter your choice: ")
    player2_choice = input("Player 2, enter your choice: ")

    player1_choice = player1_choice.upper()
    player2_choice = player2_choice.upper()

    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == 'R' and player2_choice == 'S') or (player1_choice == 'S' and player2_choice == 'P') or (player1_choice == 'P' and player2_choice == 'R'):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1

        print("Player 1: " + str(player1_score) + " | Player 2: " + str(player2_score))

    if player1_score == 3 or player2_score == 3:
        break

if player1_score == 3:
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")