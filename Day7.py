#Day 7 of 100 days of code
#Hangman

import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)

#Creating Blanks
display = []
for char in chosen_word:
  display.append("_")

end_of_game = False
lives = 6

while not end_of_game:
    guess = (input("Guess a letter: ")).lower()
    if guess in display:
      print(f"You have already guessed {guess}.")
#check guessed letter
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if guess == letter:
        display[position] = letter


    if guess not in chosen_word:
      print(f"{guess} not in word. You lose a life.")
      lives = lives - 1
      if lives == 0:
        end_of_game = True
        print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

#Display ASCI
    print(stages[lives])
