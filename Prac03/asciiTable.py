def get_number(user_input_lower, user_input_upper):

    valid_number = False

    while valid_number is False:

        try:
            user_input = int(input("Enter a number ({0}-{1}): ".format(user_input_lower, user_input_upper)))

            while user_input_lower > user_input or user_input > user_input_upper:
                print("Please enter a valid number...")
                user_input = int(input("Enter a number ({0}-{1}): ".format(user_input_lower, user_input_upper)))

            valid_number = True

        except ValueError:
            print("Please enter a valid number...")

    prints_output(user_input)

def prints_output(user_input):
    print("{}{:>8s}".format("Value", "ASCII"))
    print("{:4d} {:>6s}".format(user_input, chr(user_input)))

get_number(10, 100)


