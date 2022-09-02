print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("Will you go left or right? R or L \n")

if direction == "L":
  swim = input("Will you swin or wait? S or W \n")
  if swim == "W":
    door = input("Which colour door will you choose? R, B or Y \n")
    if door == "Y":
      print("You win!")
    elif door == "R":
      print("Burned by fire! Game over.")
    elif door == "B":
      print("Eaten by beasts! Game over.")
    else:
      print("Game over.")
  else:
    print("Attacked by Trout! Game over.")
else: 
  print("Fallen into a hole! Game over.")

