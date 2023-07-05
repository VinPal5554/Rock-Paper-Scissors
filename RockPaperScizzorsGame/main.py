import random

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

player_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors ")
player_choice_int = int(player_choice)

if player_choice_int == 0:
    print(rock)
elif player_choice_int == 1:
    print(paper)
else:
    print(scissors)


print("Computer chose:")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


if ((player_choice_int == 0 and computer_choice == 2) or (player_choice_int == 1 and computer_choice == 0) or (player_choice_int == 2 and computer_choice == 1)):
    print("You win")
elif ((player_choice_int == 0 and computer_choice == 1) or (player_choice_int == 1 and computer_choice == 2) or (player_choice_int == 2 and computer_choice == 0)):
    print("You lose")
else:
    print("Draw")