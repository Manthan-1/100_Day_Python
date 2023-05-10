#For Loop
#eg:
"""fruits = ["Apple", "Grapes", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")"""

#Practice: Avegrage Height
"""student_heights = input("Enter the list of student heights in cm ").split()
for n in range(0 , len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height = total_height + height
print("Total height = ", total_height, "cm")

number_of_student = len(student_heights)
average_height = round(total_height / number_of_student)
print("Average Height = ", average_height,"cm")"""

#Practice: Highest score
"""student_scores = input("Input a list of students scores ")
for n in range (0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print("The highest score of the class is: ", highest_score)"""

#Loop :
#Syntax = 
#for number in ranger(a, b, c):
#  print (number)
# a->b is the range and c is the step size. 

#adding all the numbers from 1->100

"""total = 0
for number in range (1,101):
  total += number 
print(total)"""

#Practice: Adding even number
"""total = 0 
for number in range (1, 101):
  if number % 2 == 0:
      total += number
print(total)"""

#Practice: The FzuuBuzz Job Interview:

for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  

    



