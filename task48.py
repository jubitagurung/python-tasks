import random
#guessing secrect number
guess = int(input("guess a secrect_number from 1 to 100:"))
secrect_number = random.randint(1,100)
guess = 0
while guess != secrect_number:
    if guess < secrect_number:
        print("You lose, it is too low!")
    elif guess > secrect_number:
        print("You lose, it is too high!")
    else:
        print("Congrats, you won!")
    print("Gameover!")