import random


num = random.randint(1, 100)
counter = 1

user_guess = int(input("guess a number 1-100: "))

while True:
    if user_guess > num:
        print("High")
        user_guess = int(input("guess a number: "))
        counter = counter + 1
    if user_guess < num:
        print("Low")
        user_guess = int(input("guess a number: "))
        counter = counter + 1
    if user_guess == num:
        print("Winner!")
        print(f"it took you {counter} guesses")
        game_status = input("Want to play again? Y or N: ").capitalize()
        if game_status.startswith("Y"):
            print("Lets play another!")
            num = random.randint(1, 100)
            user_guess = int(input("guess a number 1-100: "))
            counter = 1
        else:
            print("GAME OVER")
            break
