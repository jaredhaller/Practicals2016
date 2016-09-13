user_numbers = []

for i in range(5):
    number = int(input("Number: "))
    user_numbers.append(number)

print("The first number is {}".format(user_numbers[0]))
print("The last number is {}".format(user_numbers[-1]))
print("The smallest number is {}".format(min(user_numbers)))
print("The largest number is {}".format(max(user_numbers)))

#Is there an average function?
print("The average number is {}".format((sum(user_numbers))/5))