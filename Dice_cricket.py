import random
print("welcome to dice cricket, Good luck : )")
dice_option = 0
score = 0
while dice_option !=5:
    user_rolls = input("please enter R to roll the dice, Q to quit the game: ").upper()
    if user_rolls=='R':
        dice_option = random.randint(1,6)
        if dice_option != 5:
            score = score + dice_option
            print(f"you scored {dice_option} runs, your current score is {score}")
        else:
            print(f"sorry, you are declared out, your final score is {score}")
            break
    elif user_rolls == 'Q':
            print("you have decided to quit the game, see you soon again")
            break
print("***************Game Over*******************")