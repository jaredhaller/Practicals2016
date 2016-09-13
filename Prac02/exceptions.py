try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    #Question 3
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter a non 0 integer: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

#NOT NEEDED
#except ZeroDivisionError:
    #print("Cannot divide by zero!")

print("Finished.")

#Question 1: Occurs when the input is a non integer value. ie character, float
#Question 2: Occurs when the correct input is made, however the denominator is 0
