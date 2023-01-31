import sys

def main():
    """ Welcome script to start program """
    print()
    print("Welcome to the currency conversion calculator")

    while True:
        user_input = input("Type 'Start' to continue or 'Exit' to end the program\n")
        if user_input.lower() == "start":
            start_calculator()
            # ask if they want to continue or exit the program

        elif user_input.lower() == "exit":
            sys.exit("Ending currency conversion calculator program\n"
                     "Thank you for using the calculator!")
        else:
            print(f"{user_input} is not a valid selection")

def menu():
    """ Display main program menu to user """
    menu = {
        0: "Guided calculator",
        1: "Choose starting currency",
        2: "Enter starting amount",
        3: "Choose end currency",
        4: "Display conversion amount",
        5: "Undo start amount change",
        6: "Redo start amount change",
        7: "Help guide",
        8: "Exit calculator program"
    }
    return menu

def start_calculator():
    """ Start calculator program """
    start_currency = None
    end_currency = None
    start_amount = 0

    prev_start_amount = 0

    while True:
        print()
        print("Conversion Calculator Task Page Menu")
        for num, selection in menu().items():
            print(f"{num}: {selection}")

        print()
        print(f"Start currency: {start_currency}")
        print(f"End currency: {end_currency}")
        print(f"Amount to convert: {start_amount}")
        print()

        user_choice = int(input("Type in a number from the menu to perform the indicated tasks\n"
                            "Edit selections and entered amount by returning to task page\n"
                            "Calculations are finalized once 'Display conversion amount' is chosen\n"))

        if user_choice == 0:
            # take user step by step from selecting currency to displaying the end result
            # demo of how it should look
            demo()
        elif user_choice == 1:
            # go to page to choose a start currency
            pass
        elif user_choice == 2:
            amount_input = int(input("\nEnter amount you want to convert\n"))
            # save current start amount in case you want to undo a change
            if start_amount != 0:
                prev_start_amount = start_amount
            # change start amount
            start_amount = amount_input
        elif user_choice == 3:
            # go to page to choose end currency
            pass
        elif user_choice == 4:
            # display conversion amount
            # reset all variables
            start_currency = None
            end_currency = None
            start_amount = 0
            pass
        elif user_choice == 5:
            # undo last change
            if prev_start_amount != 0:
                # save current start amount
                temp = start_amount
                # set previous amount to start amount
                start_amount = prev_start_amount
                # set new previous amount
                prev_start_amount = temp

        elif user_choice == 6:
            # redo last change
            if prev_start_amount != 0:
                # save current start amount
                temp = start_amount
                # set previous amount to start amount
                start_amount = prev_start_amount
                # set new previous amount
                prev_start_amount = temp
        elif user_choice == 7:
            # open help guide
            help_guide_interactive()
        elif user_choice == 8:
            sys.exit("Ending currency conversion calculator program\n"
                     "Thank you for using the calculator!")
        else:
            print(f"{user_choice} is not a choice on the menu\n"
                  f"Please type in a valid selection")


def help_guide():
    """ Return help guide """
    # print("Currency Conversion Calculator Health Guide")
    # int: helpful tips (str)
    help_guide = {
        1: "How to select a start / end currency",
        2: "How to enter an amount to convert",
        3: "How to display conversion results",
        4: "How to change currency selection",
        5: "How to change amount to convert",
        6: "How to exit the calculator conversion program",
        7: "Back to main"
    }
    return help_guide

def help_guide_interactive():
    """ Interactive component for user to go through help guide """
    print()
    print("Help Guide Menu")
    for num, selection in help_guide().items():
        print(f"{num}: {selection}")
    print()

    user_choice = int(input("Type in a number from the menu to open a help page\n"))

    # if-elif-else to each menu item
    if user_choice == 1:
        print(how_to_select_currency())
        # check if user wants to return to help menu
        while True:
            user_input = input()
            if user_input.lower() == "back":
                help_guide_interactive()
            # elif user_input == "main":
            #     start_calculator()
            else:
                print("please enter 'Back' to return to go back to the help menu")
    elif user_choice == 7:
        start_calculator()

def how_to_select_currency():
    """ Return help page for selecting a currency"""
    script = "\nHow to Select a Start or End Currency\n\n" \
             "1a. Type in '1' to select a start currency\n" \
             "1b. Type in '2' to select an end currency\n" \
             "2. Browse the menu of supported currency\n" \
             "3. Type in the number that corresponds to the currency you'd like to select\n" \
             "4. You will automatically be taken back to the main menu page after entering a valid selection\n\n" \
             "Enter 'Back' to return back to the help menu\n"
    return script

def demo():
    # select starting currency
    print()
    print(f"Start currency: None")
    print(f"Amount to convert: 0")
    print(f"End currency: None")
    print()
    currencies = {
        1: "US Dollar",
        2: "Pound Sterling",
        3: "Canadian Dollar",
        4: "Japanese Yen"
    }
    for num, currency in currencies.items():
        print(f"{num}: {currency}")
    starting_currency = int(input("Type in number that corresponds to starting currency\n"))

    # enter starting amount
    print(f"Start currency: US Dollar")
    print(f"Amount to convert: 0")
    print(f"End currency: None")
    starting_amount = int(input("Type in starting amount\n"))

    # select ending currency
    print(f"Start currency: US Dollar")
    print(f"Amount to convert: 10")
    print(f"End currency: None")
    ending_currency = int(input("Type in ending currency\n"))

    # display results
    # $10
    # 8.08 pounc
    print(f"Start currency: US Dollar")
    print(f"End currency: 10")
    print(f"Amount to convert: British Pound")
    print()
    print(f"Result: £8.08")
    # 'back' to go back to main menu
    go_back = input("Type in 'back' to return to main menu\n")
    if go_back.lower() == "back":
        start_calculator()


if __name__ == "__main__":
    main()
