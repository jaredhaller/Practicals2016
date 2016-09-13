#user_input = input("Enter a Number: ")

valid_input = False

while not valid_input:
    try:
        user_input = int(input("Enter a Whole Number: "))
        valid_input = True
    except ValueError:
        print("Invalid Input")

print("Number: {}".format(user_input))