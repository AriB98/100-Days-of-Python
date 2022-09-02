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

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("error")


comp_choice = random.randint(0, 2)
if comp_choice == 0:
  print(f"Computer chose: {rock}")
elif comp_choice == 1:
  print(f"Computer chose: {paper}")
else:
  print(f"Computer chose: {scissors}")

if choice == comp_choice:
  print("Tie")
elif choice == 0 and comp_choice == 1:
  print("You Lose")
elif choice == 1 and comp_choice == 0:
  print("You win!")
elif choice == 0 and comp_choice == 2:
  print("You win!")
elif choice == 2 and comp_choice == 0:
  print("You lose")
elif choice == 1 and comp_choice == 2:
  print("You lose")
elif choice == 2 and comp_choice == 0:
  print("You win!")


'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

'''