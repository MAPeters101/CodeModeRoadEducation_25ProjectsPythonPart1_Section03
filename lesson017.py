import random

# create a variable and name it something like "computerChoice". Store a random integer between 1 and 3 in the variable.
computerChoice = random.randint(1,3)

# ask the user for their choice (if they choose rock, make them type 1, if they choose paper, make them type 2, and if they choose scissor, make them type 3)
userChoice = int(input("Please select Rock (1), Paper (2), or Scissors (3): "))

# check if the user entered a number between 1 and 3. if they didn't, then tell them that they have to restart and to "follow instructions"
if userChoice < 1 or userChoice > 3:
    print("Invalid choice!  Please restart the game and pick 1-3.")

# else, first print out the computers choice (rock if the random integer    was 1, paper if the random integer was 2, and scissor if the random        integer was 3)
else:
    if computerChoice == 1:
        print("Computer chose rock.")
    elif computerChoice == 2:
        print("Computer chose paper.")
    elif computerChoice == 3:
        print("Computer chose scissors.")

    # then check each possibility, and output who won in each of these possibilities

    # if the user entered 1 and computer entered 1 then it is a tie game
    if userChoice == 1 and computerChoice == 1:
        print("Tie Game")

    # if the user entered 2 and computer entered 2 then it is a tie game
    elif userChoice == 2 and computerChoice == 2:
        print("Tie Game")

    # if the user entered 3 and computer entered 3 then it is a tie game
    elif userChoice == 3 and computerChoice == 3:
        print("Tie Game")

    # if the user entered 1 and computer entered 2 then the computer won
    elif userChoice == 1 and computerChoice == 2:
        print("Computer Won")

    # if the user entered 2 and computer entered 3 then the computer won
    elif userChoice == 2 and computerChoice == 3:
        print("Computer Won")

    # if the user entered 3 and computer entered 1 then the computer won
    elif userChoice == 3 and computerChoice == 1:
        print("Computer Won")

    # if the user entered 1 and computer entered 3 then the user won
    elif userChoice == 1 and computerChoice == 3:
        print("User Won")

    # if the user entered 2 and computer entered 1 then the user won
    elif userChoice == 2 and computerChoice == 1:
        print("User Won")

    # if the user entered 3 and computer entered 2 then the user won
    elif userChoice == 3 and computerChoice == 2:
        print("User Won")
