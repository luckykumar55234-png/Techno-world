# import random

# number = random.randint(1, 100)

# while True:
#     guess = int(input("Guess a number (1-100): "))



#




import random

while True:
    number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number (1-100): "))

        if guess == number:
            print("Congratulations! You Win")
            break

        elif guess > number:
            print("Too High! Try Again")
        elif guess < number:
            print("Too Low! Try Again")

        else:
            print("guess Invalid Input")

    choice = input("Do you want to play again? (yes/no): ")

    if choice == "no":
        print("Game Over! Thank You")
        break

    elif choice == "yes":
        print("New Game Started")

    else:
        print("Invalid Input")
