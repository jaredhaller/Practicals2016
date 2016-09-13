print("Please enter a valid password")
print("Your password must be between 2 and 6 characters, and contain:")
print("\t1 or more uppercase characters")
print("\t1 or more lowercase characters")
print("\t1 or more numbers")

user_input = input(">>> ")

password_status = False
lower_case = False
upper_case = False
number = False
special_characters = False

while password_status is False:
    for character in user_input:
        if character.islower():
            lower_case = True
        if character.isupper():
            upper_case = True
        if character.isdigit():
            number = True
        if character in "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|":
            special_characters = True

    if lower_case and upper_case and number and special_characters:
        password_status = True

    else:
        print("Invalid Input")
        user_input = input(">>> ")

print("Your {} character password is valid: {}".format(len(user_input), user_input))