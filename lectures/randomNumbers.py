import random

#help(random)
# low = 1
# high = 100
#number = random.randint(low,high)

#random floating number:
# number1= random.random()
# print(number1)

# options=("rock", "paper", "scissors")
# cards= ["2","3","4","5","7","6","8","J","Q","K",]
# random.shuffle(cards)
# print(cards)
# option= random.choice(options)
# print(option)

## Number Guessing Game

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num,highest_num)
# guesses = 0
# is_running = True
#
# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running:
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses+=1
#         if guess<lowest_num or guess>highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess<answer:
#             print("Too low try again")
#         elif guess>answer:
#             print("Too high try again")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")

## rock, paper, scissors game

# options=("rock", "paper", "scissors")
# running = True
#
# while running:
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter a choise (rock, paper or scissors): ").lower()
#
#     print(f'Players choice is: {player}')
#     print(f"Computers choice is: {computer}")
#
#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#     if not input("Play again? (y/n): ").lower() == "y":
#         running=False
#
# print("Thanks for playing!")

## dice roller program

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
#
# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
dice = []
total = 0
num_of_dice = int(input("Enter num of dice: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for line in range (5):
    for die in dice:
       print(dice_art.get(die)[line], end= "")
    print()

for die in dice:
    total+=die
print(f"total: {total}")