print("Welcome to Video Game Age Verification!\n")

age = int(input("Enter your age to see what games you can play: "))

animalCrossing = False
superMario = False
roblox = False
fortnite = False
callOfDuty = False
# your first condition statement will simply check to see if the user is between the ages of 0 - 17 (greater than or equal to 0 and less than or equal to 17) If this condition is false, then the rest of the program should not run. The rest of your program should be wrapped inside of this first if statement!
if 0 <= age <= 17:
    # check if the user is old enough to play Animal Crossing (0 years old minimum). If so, keep the animalCrossing variable as True. Otherwise, set it equal to false. It is currently set to True as default
    animalCrossing = True

    # check if the user is old enough to play Super Mario Odyssey (10 years old minimum). If so, keep the superMario variable as True. Otherwise, set it equal to false. It is currently set to True as default.
    if age >= 10:
        superMario = True

    # check if the user is old enough to play Fortnite (12 years old minimum). If so, keep the fortnite variable as True. Otherwise, set it equal to false. It is currently set to True as default
    if age >= 12:
        fortnite = True

    # check if the user is old enough to play Roblox (10 years old minimum). If so, keep the roblox variable as True. Otherwise, set it equal to false. It is currently set to True as default
    if age >= 10:
        roblox = True

    # check if the user is old enough to play Call Of Duty (17 years old minimum). If so, keep the callOfDuty variable as True. Otherwise, set it equal to false. It is currently set to True as default
    if age >= 17:
        callOfDuty = True

    # use the logical "and" operator to check if all 5 of the boolean variables are equal to true. If so, simply print that the user is allowed to play every video game.
    if animalCrossing and superMario and fortnite and roblox and callOfDuty:
        print("The user is allowed to play every video game.")
    # else, print the specific video games that the user can play. HINT: You will only need 4 if statements for this section becuase 17 year olds can play every game.
    else:
        if animalCrossing:
            print("The user can play Animal Crossing.")
        if superMario:
            print("The user can play Super Mario.")
        if fortnite:
            print("The user can play Fortnight.")
        if roblox:
            print("The user can play Roblox.")


