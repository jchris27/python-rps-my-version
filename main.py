rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_hand = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
user_picks = int(user_hand)

computer_hand = [rock, paper, scissors]
computer_chose = len(computer_hand) - 1
computer = random.randint(0, computer_chose)
ai = computer_hand[computer]


if user_picks == 0:
  print(rock)
  print("Computer chose:")
  print(ai)
elif user_picks == 1:
  print(paper)
  print("Computer chose:")
  print(ai)
elif user_picks == 2:
  print(scissors)
  print("Computer chose:")
  print(ai)
else:
  print("Sorry wrong input. Try again!")

if user_picks == 0 and computer == 2:
  print("You Won!")
elif user_picks == 1 and computer == 0:
  print("You Won!")
elif user_picks == 2 and computer == 1:
  print("You Won!")
elif user_picks == computer:
  print("It's a draw.")
else:
  print("You lose.")


