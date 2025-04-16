#Individual Assignment 7 - A die game between two players
import random

# Function to simulate rolling the dice
def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

# Function to play a single round of rolling a die
def play_round(player1, player2):
    """Determines the winner of dice game."""
    
    if player1 == player2:  
        print(f"Both players rolled {player1}. The round is a tie.") #If player 1 and player 2 roll same number, print about they are tie.
    elif player1 > player2:
        print(f'Player 1 rolled {player1}, Player 2 rolled {player2}. Player 1 wins the round.') #If player 1 roll bigger number than player 2, print about player 1 wins.
    else:
        print(f'Player 1 rolled {player1}, Player 2 rolled {player2}. Player 2 wins the round.') #If player 2 roll bigger number than player 1, print about player 2 wins.

# Main function to orchestrate dice game
def main():
    player1_score = 0 #A variable for recording the number of player 1's winning round
    player2_score = 0 #A variable for recording the number of player 2's winning round
    tie_score = 0 #A variable for recording the number of tieing round

    # Ask the user for the number of rounds
    rounds = int(input("How many rounds do you want to play? "))

    #Loop function for the recording the dice game's result
    for _ in range(rounds):
        player1 = roll_dice()
        player2 = roll_dice()
        if player1 == player2:
            tie_score += 1
        elif player1 > player2:
            player1_score += 1
        else:
            player2_score += 1

        #Call the play_round function
        play_round(player1, player2)

    # Print the final results
    print(f"\nFinal Score: Player 1 wins {player1_score} round(s). Player 2 wins {player2_score} round(s). {tie_score} round(s) ended in a tie.")
    if player1_score > player2_score:
        print("Overall Winner: Player 1!")
    elif player2_score > player1_score:
        print("Overall Winner: Player 2!")
    else:
        print("The game ends in a tie!")

#Call the main function
if __name__ == "__main__":
    main()