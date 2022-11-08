from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print (logo)

name = input("What is your name? \n")
bid = input("What is your bid price? \n $") 

bids_dict = {}
bids_dict[name] = bid


user_presence = input("Are there other users that want to bid?")
                 

while user_presence == "yes":
  clear()
  name = input("What is your name? \n")
  bid = input("What is your bid price?   \n $") 

  bids_dict = {}
  bids_dict[name] = bid
  user_presence = input("Are there other users that want to bid?")

else:
  winner = max(bids_dict)
  highest_bid = max(bids_dict.values())
  print(f"The wiiner is {winner} with a bid of: ${highest_bid}")
