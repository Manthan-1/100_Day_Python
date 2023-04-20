# Day 3 Practice : ControlFlow

#if..else...

# Syntax: 
#if condition: 
#  do this
#elif condition: 
#  do this
#else: 
#  do this

#Practice 3.1: If..else
"""print("Welcome to the rollercoaster ride!! ")
height = int(input("what is you height in cm? ")) 
if height > 120:
  print("You can ride the rollercoaster!!")
elif height == 120:
  print("You can ride the rollercoaster!!")
else:
  print("Sorry, you can't ride the rollercoaster.")"""

#Practice 3.2: Given number is odd or even 
"""number = int(input("Enter the number. "))
if (number % 2) == 0:
  print("Its a even number ! ")
else:
  print("Its a odd number ! ")"""

#Nested if statement:
"""print("Welcome to the rollercoaster ride!! ")
height = int(input("what is you height in cm? ")) 
if height > 120:
  print("You can ride the rollercoaster ! ")
  age = int(input("Enter your age. "))
  if age > 18:
    print("Your ticket price is $12")
  elif age > 12 and age < 18:
    print("Your Ticket price is $7")
  else: 
    print("Your Ticket price is $5")
else: 
  print("Sorry, you can't ride the rollercoaster.")"""

#Practice: BMI Calculator with results 
"""weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight/height**2)
print(bmi)

if bmi <= 18.5:
  print("Underweight.")
elif bmi <= 25:
  print("Normal weight.")
elif bmi <= 30:
  print("Overweight.")
elif bmi <= 35:
  print("Obese.")
else:
  print("Clinically Obese.")"""

#Practice: Leap year:
"""year = int(input("Enter the year you want to check. "))

if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap Year!")
      else:
        print("Not a leap Year!")
    else:
      print("Its a leap Year!")
else:
  print("Not a leap year! ")"""

#Practice: Multiple if

"""print("Welcome to the rollercoaster ride!! ")
height = int(input("what is you height in cm? ")) 
bill = 0
if height > 120:
  print("You can ride the rollercoaster ! ")
  age = int(input("Enter your age. "))
  if age > 18:
    bill = 12
    print("Adult ticket is $12. ")
  
  elif age > 12 and age < 18:
    bill = 7
    print("Teenager ticket is $7. ")

  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!  ")
  
  else:
    bill = 5
    print("Children ticket is $5")

  print("The photo cost is $3.")
  photo = input("Do you want a photo to be taken? Y/N ")
  if photo == "Y": 
    bill = bill + 3
    print("Your total bill is $", bill )
  else: 
    print("Your total bill is $",bill )  
else: 
  print("Sorry, you can't ride the rollercoaster.")"""

#Practice: Pizza delivery
# small pizza: 15
# Medium pizza: 20
# large pizza: 25
# pepperoni for small pizza: 2
# pepperoni for medium or large pizza: 3
# extra cheese for any size pizza:1

"""print("Welcmome to pizza delivery ")
size = input("What size of pizza do you want? Small, Medium, Large? ")
addPepperoni = input("Do you want pepperoni? Y/N ")
print("Added Extra cheese is $1")
addCheese = input("Do you want extra cheese? Y/N ")
bill = 0
if size == "Small":
  bill = 15
  print("Price of small pizza is $15 ")
  if addPepperoni == "Y":
    print("Added pepperoni it's extra $2")
    bill += 2
    print("Your bill so far is $", bill)
  else: 
    print("Your bill so far is $", bill)
      
if size == "Medium":
  bill = 20
  print("Price of medium pizza is $20 ")
  if addPepperoni == "Y":
    print("Added pepperoni it's extra $3")
    bill += 3
    print("Your bill so far is $", bill)
  else: 
    print("Your bill so far is $", bill)
      
if size == "Large":
  bill = 25
  print("Price of large pizza is $25 ")
  
  if addPepperoni == "Y":
    print("Added pepperoni it's extra $3")
    bill += 3
    print("Your bill so far is $", bill)
  else: 
    print("Your bill so far is $", bill)
  
  if addCheese == "Y":
    bill += 1
    print("Your Total bill is $", bill)
  else: 
    print("Your Total bill is $", bill)"""

# Practice: Love Calculator

print("Welcome to love calculator!!")
person1 = input("Enter 1st name: \n")
person2 = input("Enter 2nd name: \n")

name1 = person1.lower() #is used to store name in lower case 
name2 = person2.lower() #is used to store name in lower case

combined_name = name1 + name2

T = combined_name.count("t")
R = combined_name.count("r")
U = combined_name.count("u")
E = combined_name.count("e")
true = T + R + U + E

L = combined_name.count("l")
O = combined_name.count("o")
V = combined_name.count("v")
E = combined_name.count("e")
love = L + O + V + E

loveScore = str(true) + str(love)
int_loveScore = int(loveScore)

if (int_loveScore < 10) or (int_loveScore > 90):
  print("Your score is ", int_loveScore, "You go togerther like coke and mentos. ")

elif int_loveScore >= 40 and int_loveScore <= 50:
  print("Your score is ", int_loveScore, "you are alright together. ")
else:
  print("Your love score is ", int_loveScore)      