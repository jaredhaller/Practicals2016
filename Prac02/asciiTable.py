lower = 10
upper = 100

user_input = int(input("Enter a number ({0}-{1}): ".format(lower,upper)))
print("{}{:>8s}".format("Value", "ASCII"))
print("{:4d} {:>6s}".format(user_input, chr(user_input)))
