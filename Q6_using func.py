p1 = input("Player 1, choose rock, paper, or scissors: ")
p2 = input("Player 2, choose rock, paper, or scissors: ")

def play(player1, player2):
    if player1 == player2:
        print("play again")

    elif player1 == 'rock':
        if player2 == 'scissors':
            print("Rock hits scissors. Player 1 win!")

    elif player1 == 'paper':
        if player2 == 'scissors':
            print("Scissors cut paper. Player 2 wins")

    elif player1 == 'scissors':
        if player2 == 'rock':
            print("Rock hits scissors. Player 2 wins!")

    elif player1 == 'rock':
        if player2 == 'paper':
            print("Paper covers rock. Player 2 wins!")

    elif player1 == 'scissors':
        if player2 == 'paper':
            print("Scissors cut paper. Player 1 wins!")

    elif player1 == 'paper':
        if player2 == 'rock':
            print("Paper covers rock. Player 1 wins!")
        else:
            return "Paper wins"
    else:
        print("Invalid choice")
        return play(p1, p2)


print(play(p1, p2))