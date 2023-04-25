# Game: Rock, Paper & Scissors
import random

rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
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

user_input = int(input("Enter your choise. \nType 0 for rock, Type 1 for paper, Type 2 for scissors "))
if user_input == 0:
  print("You have chosen rock\n", rock)
elif user_input == 1:
  print("You have chosen paper\n", paper)
else:
  print("You have chosen scissors\n", scissors)

Computer_Choise = random.randint(0,2)
print(Computer_Choise)
if Computer_Choise == 0:
  print("Computer has chosen rock\n", rock)
elif Computer_Choise == 1:
  print("Computer has chosen paper\n", paper)
else:
  print("Computer has chosen scissors\n", scissors)

#Rock Case
if user_input == Computer_Choise:
  print("It's a Draw!!")
elif user_input == 0 and Computer_Choise == 1:
  print("Computer won the game!!")
elif user_input == 0 and Computer_Choise == 2:
  print("You won the game!!")

#Paper Case
if user_input == 1 and Computer_Choise == 0:
  print("You won the game!!")
elif user_input == Computer_Choise:
  print("It's a draw!!")
elif user_input == 1 and Computer_Choise == 2:
  print("Computer won the game!!")


#Scissors Case
if user_input == 2 and Computer_Choise == 0:
  print("Computer won the game!!")
elif user_input == 2 and Computer_Choise == 1:
  print("You won the game!!")
elif user_input == Computer_Choise:
  print("It's a draw!!")