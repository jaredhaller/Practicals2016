"""
Do-From Scratch Exercises
"""

#Question 1
users_name = input("What is your name: ")
name_file = open("name.txt", "w")
print(users_name, file=name_file)
name_file.close()

#Question 2
name_file = open("name.txt", "r")
txt_data = name_file.readline()
name_file = open("name.txt", "a")
print("Your name is {}".format(txt_data), file=name_file)
name_file.close()

#Question 3
numbers_file = open("numbers.txt", 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print("Question 3 answer {}".format(number1 + number2))

#Question 3 Extented
numbers_total = 0

numbers_file = open("numbers.txt", 'r')
for numbers in numbers_file:
    numbers_total += int(numbers)

numbers_file.close()
print("Question 3E answer {}".format(numbers_total))
