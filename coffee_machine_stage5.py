"""
Stage 5:
Write a program that will work endlessly to make coffee for all
interested persons until the shutdown signal is given.
Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee.
If the coffee machine doesn't have enough resources to make coffee,
the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy"
to buy a cup of coffee and then changes his mind,
hey should be able to type "back" to return into the main cycle
"""


def remaining_menu():
    """ print out the summary menu of ingredients """

    global amt_of_water_FINAL
    global amt_of_beans_FINAL
    global amt_of_milk_FINAL
    global amt_of_cups_FINAL
    global money_FINAL

    print('The coffee machine has:')
    print('{} of water'.format(amt_of_water_FINAL))
    print('{} of milk'.format(amt_of_milk_FINAL))
    print('{} of coffee beans'.format(amt_of_beans_FINAL))
    print('{} of disposable cups'.format(amt_of_cups_FINAL))
    print('${} of money'.format(money_FINAL) if money_FINAL > 0 else
          '{} of money'.format(money_FINAL))
    print()  # formatting


def buy():
    """ main code logic for buying coffee from coffee machine """

    # set "global" keyword to use variables in function!
    global amt_of_water_FINAL
    global amt_of_beans_FINAL
    global amt_of_milk_FINAL
    global amt_of_cups_FINAL
    global money_FINAL

    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::')
    action = input()  # find out which option to operate
    if action == '1':  # espresso option
        if amt_of_water_FINAL >= 250 and amt_of_beans_FINAL >= 16:
            amt_of_water_FINAL -= 250
            amt_of_beans_FINAL -= 16
            money_FINAL += 4
            amt_of_cups_FINAL -= 1
            print('I have enough resources, making you a coffee!')
            print()  # formatting
        else:
            if amt_of_water_FINAL < 250:
                print('Sorry, not enough water!')
            elif amt_of_beans_FINAL < 16:
                print('Sorry, not enough coffee beans!')
            print()  # formatting
    elif action == '2':  # latte option
        if amt_of_water_FINAL >= 350 and amt_of_milk_FINAL >= 75 and amt_of_beans_FINAL >= 16:
            amt_of_water_FINAL -= 350
            amt_of_milk_FINAL -= 75
            amt_of_beans_FINAL -= 20
            money_FINAL += 7
            amt_of_cups_FINAL -= 1
            print('I have enough resources, making you a coffee!')
            print()  # formatting
        else:
            if amt_of_water_FINAL < 250:
                print('Sorry, not enough water!')
            elif amt_of_beans_FINAL < 16:
                print('Sorry, not enough coffee beans!')
            elif amt_of_milk_FINAL < 75:
                print('Sorry, not enough milk!')
            print()  # formatting
    elif action == '3':  # cappuccino option
        if amt_of_water_FINAL >= 200 and amt_of_milk_FINAL >= 100 and amt_of_beans_FINAL >= 12:
            amt_of_water_FINAL -= 200
            amt_of_milk_FINAL -= 100
            amt_of_beans_FINAL -= 12
            money_FINAL += 6
            amt_of_cups_FINAL -= 1
            print('I have enough resources, making you a coffee!')
            print()  # formatting
        else:
            if amt_of_water_FINAL < 250:
                print('Sorry, not enough water!')
            elif amt_of_beans_FINAL < 12:
                print('Sorry, not enough coffee beans!')
            elif amt_of_milk_FINAL < 100:
                print('Sorry, not enough milk!')
            print()  # formatting
    else:  # 'back' option - go back to main page (do nothing)
        print()  # formatting
        pass

    # print out updated menu
    # remaining_menu()


def fill():
    """ main code logic for refilling coffee machine """

    global amt_of_water_FINAL
    global amt_of_beans_FINAL
    global amt_of_milk_FINAL
    global amt_of_cups_FINAL

    print('Write how many ml of water do you want to add:')
    amt_of_water_to_add = int(input())
    print('Write how many ml of milk do you want to add:')
    amt_of_milk_to_add = int(input())
    print('Write how many grams of coffee beans do you want to add::')
    amt_of_beans_to_add = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    amt_of_cups_to_add = int(input())

    # update the numbers
    amt_of_water_FINAL += amt_of_water_to_add
    amt_of_milk_FINAL += amt_of_milk_to_add
    amt_of_beans_FINAL += amt_of_beans_to_add
    amt_of_cups_FINAL += amt_of_cups_to_add

    # formatting
    print()


def take():
    """ main code logic for collecting coffee machine's revenue """

    global money_FINAL

    print('I gave you ${}'.format(money_FINAL))
    # update money to 0
    money_FINAL = 0
    # formatting
    print()


def main():
    """ to run main code """

    # simulate the repeating loop to call for user's input
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()  # retrieve the action to operate
        print()  # leave a space for formatting

        # execute options
        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'remaining':
            remaining_menu()
        elif action == 'exit':
            exit()  # exit program
        else:  # exception case where user types in none of the above
            print('No menu found for option!')
            print()  # formatting


# set the initial parameters
amt_of_water_FINAL = 400
amt_of_milk_FINAL = 540
amt_of_beans_FINAL = 120
amt_of_cups_FINAL = 9
money_FINAL = 550

main()
