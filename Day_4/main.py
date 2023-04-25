# Day 4: Randomisaion and Python List

#Random mudolue: you have to import it using "import random"

"""import random

random_integer = random.randint(1,100)
print(random_integer)

# random float has a range of 0.000-0.99999
random_float = random.random()
#printing a random floating number 1 - 5
random_float * 5
print(random_float)"""

#practice 4.1: Heads or tails
"""import random

random_number = random.randint(1,2)
if random_number == 1:
  print("Heads")
else: 
  print("Tails")"""

#Practice 4.2: Banker Roulette - who will pay the bill?

"""import random

name = input("Give me everybody's names, separated by a comma.")
name_seperator = name.split(", ")
print(name_seperator)
num_items = len(name_seperator)# get the total length of the list 

random_choice = random.randint(0, num_items - 1)
random_name = name_seperator[random_choice]
# random_name = random.choice(name_seperator)
print(random_name + " is going to pay the bill.")"""

#Nested List: 
fruits = ["Strawberries", "Apples", "Grapes", "Banana"]
vegitables = ["Potato", "Tomatoes", "Spinach"]

nested_list = [fruits , vegitables]
print(nested_list[1][1])