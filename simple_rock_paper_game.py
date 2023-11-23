while True:
    player1_choice = input("Player 1, choose rock, paper, or scissors: ")
    player2_choice = input("Player 2, choose rock, paper, or scissors: ")

    if player1_choice == player2_choice:
        result = "It's a tie!"
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"
    elif player1_choice == "scissors":
        if player2_choice == "paper":
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"
    elif player1_choice == "paper":
        if player2_choice == "rock":
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"
    else:
        result = "Invalid input! Please choose rock, paper, or scissors."

    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break