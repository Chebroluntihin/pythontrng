actions=['rock', 'paper', 'scissors']
player1=input("choose rock, paper, scissors")
player2=input("choose rock, paper, scissors")
if player1 == player2:
    print("It's a tie")

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
        print("Paper wins")
else:
    print("Invalid choice")
