def main():
    user_name = input("What is your name: ")
    prints_name(user_name)

def prints_name(user_name):
    for character in user_name[::2]:
        print(character)

main()