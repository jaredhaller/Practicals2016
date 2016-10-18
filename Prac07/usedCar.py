"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    bus = Car('Bus', 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car('Limo', 100)
    limo.fuel += 20
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    # print("Car {}, {}".format(bus.fuel, bus.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=bus))

main()