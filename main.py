def appender():
    with open("list.txt") as file:
        themes = file.readlines()

    theme = input('Theme: ').lower()
    if theme == "q":
        menu()

    elif f"{theme}\n" in themes:
        print("Theme exists.")

    else:
        with open("list.txt", "a") as file2:
            file2.write(f"{theme}\n")
        print("Theme does not exist; theme appended.")

    appender()


def solver():
    with open("list.txt") as file:
        themes = file.readlines()

    theme_possibilities = sorted([i.strip("\n") for i in themes])

    while True:
        try:
            characters = input("Characters: ")
            if characters == "q":
                menu()
            characters = int(characters)

        except ValueError:
            print("Invalid input.\n"
                  "Enter integer or 'q' to quit.")

        else:
            break

    theme_possibilities = [i for i in theme_possibilities if len(i) == characters]
    print(theme_possibilities)

    while True:
        try:
            spaces = input("Spaces: ")
            if spaces == "q":
                solver()
            spaces = int(spaces)

        except ValueError:
            print("Invalid input.\n"
                  "Enter integer or 'q' to quit.")

        else:
            break

    theme_possibilities = [i for i in theme_possibilities if i.count(" ") == spaces]
    print(theme_possibilities)

    while True:
        try:
            hint = input("Hint: ").lower()
            while hint != "q":
                place = int(hint[:len(hint)-1])
                character = hint[len(hint)-1]

                theme_possibilities = [i for i in theme_possibilities if i[place-1] == character]
                print(theme_possibilities)

                hint = input("Hint: ").lower()

        except ValueError:
            print("Invalid input.\n"
                  "Enter place and character or 'q' to quit.")

        else:
            break

    solver()


def menu():
    command = input("Option: ")
    if command == "a":
        appender()

    elif command == "s":
        solver()

    elif command == "q":
        quit()

    else:
        print("Invalid input.\n"
              "Enter 'a' to append, 's' to solve, or 'q' to quit.")
        menu()


menu()
