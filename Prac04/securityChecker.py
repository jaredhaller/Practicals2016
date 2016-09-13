def securityChecker():

    valid_usernames = ('jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                   'swei45','BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                   'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob')

    user_username = input("Username: ")

    if user_username in valid_usernames:
        print("Access Granted")
        generate_income_report()

    else:
        print("Access Denied")


def generate_income_report():
    incomes = []
    error_check = False

    #Error Handling
    while error_check is False:
        try:
            number_of_months = int(input("How many number_of_months? "))

            while number_of_months <= 0:
                print("Please input positive number of months!")
                number_of_months = int(input("How many number_of_months? "))

            error_check = True

        except ValueError:
            print("Number of months must be a number!")

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {} ".format(month)))
        incomes.append(income)

    #Call print_report function
    print_report(incomes, number_of_months, income, month)


def print_report(incomes, number_of_months, income, month):
    print("\nIncome Report\n-------------")
    total = 0

    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

securityChecker()