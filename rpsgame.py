# Julian Privitt
# 9/30/19
# Period 1
#____________________________________________________________________________________
# Break into pieces
# Welcome page, with name entry
# Score screen with Computer, player (name), ties
# Options for game r, p, s, q
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
# a choice from the player, compare the two, and update the score
# When the game is over (q is entered) final score displayed.

# Welcome Page
# prompt for the player name
# a welcome message
#____________________________________________________________________________________

# imports
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your username ")
# Main Loop
while True:
	# print score
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' for quit: ")
	computerChoice = random.choice(cChoices)
	if choice == "q":
		if playerScore > computerScore:
			print("You Win! Congratulations!")
		elif computerScore > playerScore:
			print("You lost. Better luck next time!")

		elif playerScore == computerScore:
			print("It was a tie. Better luck next time.")
		break
	
	if choice == "r":
		print(name + " picked Rock")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	if choice == "p":
		print(name + " picked Paper")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("It was a tie")
			ties = ties + 1
		else:
			print("Computer picked Scissors")
			print("Scissors beats Paper")
			computerScore += 1
	if choice == "s":
		print(name + " picked Scissors")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beats Paper")
			playerScore += 1
		else:
			print("Computer picked Scissors")
			print("It was a tie")
			ties = ties + 1