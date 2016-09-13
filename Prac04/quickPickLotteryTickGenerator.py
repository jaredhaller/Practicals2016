import random


def lottery_ticket_generator():
    error_check = False

    while error_check is False:
        try:
            number_picks = int(input("How many quick picks? "))

            while number_picks <= 0:
                print("Enter a positive number of picks!")
                number_picks = int(input("How many quick picks? "))

            error_check = True

        except ValueError:
            print("Enter a valid number of picks!")

    for picks in range(1, number_picks + 1):
        number_generator()


def number_generator():
    lottery_numbers = []
    valid_number = False

    for number in range(0, 6):
        while valid_number is False:
            lottery_numbers.append(random.randint(1, 45))
            if len(lottery_numbers) > 1:
                while lottery_numbers[-1] in lottery_numbers[:-1]:
                    lottery_numbers[-1] = random.randint(1, 45)
                valid_number = True
            else:
                valid_number = True
        valid_number = False

    lottery_numbers.sort()
    print(lottery_numbers)


lottery_ticket_generator()
