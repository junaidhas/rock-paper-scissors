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

#Write your code below this line 👇
game_continue = True
userscore = 0
computer_score =0
while game_continue:
  userplay=input("Enter your choice 0 for rock, 1 for paper and 2 for scissors: \n")

  if userplay=="exit":
    print("game is ended")
    game_continue = False
    
  computerplay=random.choice([rock, paper, scissors])
  print(f"Computer choose {computerplay}")
  
  if userplay=="0":
    print(f"your choice is rock \n {rock}")
    if computerplay==rock:
      print("Nobody wins, try playing again")
    elif computerplay==paper:
      print("Computer wins, better luck next time")
      computer_score+=1
    elif computerplay==scissors:
      print("hooray congratulations!!! You win")
      userscore+=1
    print(f"userscore = {userscore}, computer_score= {computer_score} ")
  
  elif userplay=="1":
    print(f"your choice is paper \n {paper}")
    if computerplay==rock:
      print("hooray congratulations!!! You win")
      userscore+=1
    elif computerplay==paper:
      print("Nobody wins, try playing again")
    elif computerplay==scissors:
      print("computer wins, better luck next time")
      computer_score+=1
    print(f"userscore = {userscore}, computer_score= {computer_score} ")
  
  elif userplay=="2":
    print(f"your choice is scissors \n {scissors}")
    if computerplay==rock:
      print("computer wins, better luck next time")
      computer_score+=1
    elif computerplay==paper:
      print("hooray congratulations!!! You win")
      userscore+=1
    elif computerplay==scissors:
      print("Nobody wins, try playing again")
    print(f"userscore = {userscore}, computer_score= {computer_score} " )
