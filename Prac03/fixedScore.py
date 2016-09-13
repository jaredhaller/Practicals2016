"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def user_input():
    score = float(input("Enter score: "))
    calculate_score(score)

    #HERE
    #print(status)

def calculate_score(score):
    if score < 0 or score > 100:
        status = "Invalid score"
    elif score > 90:
        status = "Excellent"
    elif score > 50:
        status = "Passable"
    else:
        status = "Pass"

    # Lindsey I was just wondering if I could put this return print(status) up ^^^^^
    return print(status)

user_input()


