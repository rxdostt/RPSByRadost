import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

choice = input("Choose [r]ock, [p]aper or [s]cissors:  ")

if choice == "r":
    choice = rock
elif choice == "p":
    choice = paper
elif choice == "s":
    choice = scissors
else:
    raise SystemError("Invalid Input. Try again..")

pc_move = ""
comp_random_input = random.randint (1,3)
if comp_random_input == 1:
    pc_move = rock
    print("AI chose Rock")
elif comp_random_input == 2:
    pc_move = paper
    print("AI chose Paper")
elif comp_random_input == 3:
    pc_move = scissors
    print("AI chose Scissors")

if (choice == rock and pc_move == scissors):
    print("You won! Well done!")
elif (choice == paper and pc_move == rock):
    print("You won! Well done!")
elif (choice == scissors and pc_move == paper):
    print("You won! Well done!")
elif (choice == rock and pc_move == paper):
    print("You lost! Give it another try")
elif (choice == scissors and pc_move == rock):
    print("You lost! Give it another try")
elif (choice == paper and pc_move == scissors):
    print("You lost! Give it another try")
elif (choice == rock and pc_move == rock):
    print("It's a draw! Try again..")
elif (choice == paper and pc_move == paper):
    print("It's a draw! Try again..")
elif (choice == scissors and pc_move == scissors):
    print("It's a draw! Try again..")
