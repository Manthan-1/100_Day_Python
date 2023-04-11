# Day 2 Practice : Data_Type, Type_Casting 

""" Data_Type: String: 
print("Hello"[0]) #string always start with 0 index.  

Data_Type: Integer: 
print(123 + 345)

Data_type: Float:
print(3.14159)

#Data_type: Boolean:
True/False #alaways starts with a capital letter"""

"""street_name = "Abbey Road"
print(street_name[4] + street_name[7])"""

#Type_Casting:

"""num_len = len(input("What is your name?"))
new_num_len = str(num_len) #converting the data type from int to str because concate doesnt work with int.
print("Your name has " + new_num_len + " characters.")"""

# Practice 2.1: Add the random two digit number

"""number = input("What is the two digit number you want to add? ")
firstDigit = int(number[0])
secondDigit = int(number[1])
result = firstDigit + secondDigit
print(result)
#Step1 : Took a two digit number from the user 
#Step2: Assigned a separate varbiable for the two digit
#Step3: Since the datatype is string in order to perform addition converted both the digits from string to number."""

#Mathematical Operation: 
# + -> Addition (Output is int)
# - -> Subtraction (Output is int)
# * -> Multiplication (Output is int)
# / -> Division (Output is float)
# ** -> Exponential (output is int)
"""Priority : PEMDAS
P = Parentheses ()
E = Exponents **
M = Multiplication *
D = Division /
A = Addition +
S = Subtraction - """

#Practice 2.2: BMI calculator 
# bmi = weight(kg) / height^2(m)
"""
weight = int(input("Please enter your weight in kg's: "))
height = float(input("Please enter your height in m's: "))
bmi = weight / (height ** 2)
print(bmi)
"""

#Practice 2.3: No. of days left
"""
age = int(input("What is your current age? "))

years_left = int(100 - age)
print(years_left)
days_left = int(years_left * 365)
print(days_left)
weeks_left = int(years_left * 52)
print(weeks_left)
months_left = int(years_left * 12)
print(months_left)

message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left"
print(message)
"""

#Project 2: Tip Calculator 

print("Welcome to tip calculator")
billAmount = float(input("What is the total bill? $"))

tipPercentage = float(input("What percentage tip would you like to give? 10, 12 or 15? ")) 

split = int(input("How many people to split the bill? "))

eachPerson = (billAmount + ((billAmount / 100) * tipPercentage)) / split
print("Each Person has to pay: $", eachPerson)


