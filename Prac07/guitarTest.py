"""
Do from scratch exercise
"""

from Prac07.guitar import Guitar


def main():

    guitar_list = []

    while True:
        name = input("Name: ")

        if not name:
            break

        year = int(input("Year: "))
        price = float(input("Price: "))
        guitar = Guitar(name, year, price)

        guitar_list.append(guitar)
        print(guitar)

    counter = 1

    for guitar in guitar_list:
        if guitar.is_vintage():
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} (vintage)".format(counter, guitar.name, guitar.year,
                                                                              guitar.cost))
        else:
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(counter, guitar.name, guitar.year, guitar.cost))

        counter += 1


main()
