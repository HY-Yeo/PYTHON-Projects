class CoffeeMachine:
    """
    Create a coffee machine class to represent the coffee machine object
    and the actions needed
    """

    # define class attributes
    n_coffee_machine = 0  # to track the number of instance of coffee machines created

    # define the default ingredient state of coffee machine
    amt_of_water_FINAL = 400
    amt_of_milk_FINAL = 540
    amt_of_beans_FINAL = 120
    amt_of_cups_FINAL = 9
    money_FINAL = 550

    # restrict to only 1 instance of a coffee machine to be created
    # objects are created by the __new__ that in turns calls the __init__ method
    def __new__(cls):
        if cls.n_coffee_machine == 0:
            cls.n_coffee_machine += 1
            return object.__new__(cls)

    # define a default constructor to initialise the coffee machine object
    def __init__(self):
        pass

    def remaining_menu(self):
        """ print out the summary menu of ingredients """

        '''
        global self.amt_of_water_FINAL
        global self.amt_of_beans_FINAL
        global self.amt_of_milk_FINAL
        global self.amt_of_cups_FINAL
        global self.money_FINAL
        '''

        print('The coffee machine has:')
        print('{} of water'.format(self.amt_of_water_FINAL))
        print('{} of milk'.format(self.amt_of_milk_FINAL))
        print('{} of coffee beans'.format(self.amt_of_beans_FINAL))
        print('{} of disposable cups'.format(self.amt_of_cups_FINAL))
        print('${} of money'.format(self.money_FINAL))
        print()  # formatting

    def buy(self):
        """ main code logic for buying coffee from coffee machine """

        '''
        # set "global" keyword to use variables in function!
        global amt_of_water_FINAL
        global amt_of_beans_FINAL
        global amt_of_milk_FINAL
        global amt_of_cups_FINAL
        global money_FINAL
        '''

        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::')
        action = input()  # find out which option to operate
        if action == '1':  # espresso option
            if self.amt_of_water_FINAL >= 250 and self.amt_of_beans_FINAL >= 16:
                self.amt_of_water_FINAL -= 250
                self.amt_of_beans_FINAL -= 16
                self.money_FINAL += 4
                self.amt_of_cups_FINAL -= 1
                print('I have enough resources, making you a coffee!')
                print()  # formatting
            else:
                if self.amt_of_water_FINAL < 250:
                    print('Sorry, not enough water!')
                elif self.amt_of_beans_FINAL < 16:
                    print('Sorry, not enough coffee beans!')
                print()  # formatting
        elif action == '2':  # latte option
            if self.amt_of_water_FINAL >= 350 and self.amt_of_milk_FINAL >= 75 and self.amt_of_beans_FINAL >= 16:
                self.amt_of_water_FINAL -= 350
                self.amt_of_milk_FINAL -= 75
                self.amt_of_beans_FINAL -= 20
                self.money_FINAL += 7
                self.amt_of_cups_FINAL -= 1
                print('I have enough resources, making you a coffee!')
                print()  # formatting
            else:
                if self.amt_of_water_FINAL < 250:
                    print('Sorry, not enough water!')
                elif self.amt_of_beans_FINAL < 16:
                    print('Sorry, not enough coffee beans!')
                elif self.amt_of_milk_FINAL < 75:
                    print('Sorry, not enough milk!')
                print()  # formatting
        elif action == '3':  # cappuccino option
            if self.amt_of_water_FINAL >= 200 and self.amt_of_milk_FINAL >= 100 and self.amt_of_beans_FINAL >= 12:
                self.amt_of_water_FINAL -= 200
                self.amt_of_milk_FINAL -= 100
                self.amt_of_beans_FINAL -= 12
                self.money_FINAL += 6
                self.amt_of_cups_FINAL -= 1
                print('I have enough resources, making you a coffee!')
                print()  # formatting
            else:
                if self.amt_of_water_FINAL < 250:
                    print('Sorry, not enough water!')
                elif self.amt_of_beans_FINAL < 12:
                    print('Sorry, not enough coffee beans!')
                elif self.amt_of_milk_FINAL < 100:
                    print('Sorry, not enough milk!')
                print()  # formatting
        else:  # 'back' option - go back to main page (do nothing)
            print()  # formatting
            pass

    def fill(self):
        """ main code logic for refilling coffee machine """

        '''
        global amt_of_water_FINAL
        global amt_of_beans_FINAL
        global amt_of_milk_FINAL
        global amt_of_cups_FINAL
        '''

        print('Write how many ml of water do you want to add:')
        amt_of_water_to_add = int(input())
        print('Write how many ml of milk do you want to add:')
        amt_of_milk_to_add = int(input())
        print('Write how many grams of coffee beans do you want to add::')
        amt_of_beans_to_add = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        amt_of_cups_to_add = int(input())

        # update the numbers
        self.amt_of_water_FINAL += amt_of_water_to_add
        self.amt_of_milk_FINAL += amt_of_milk_to_add
        self.amt_of_beans_FINAL += amt_of_beans_to_add
        self.amt_of_cups_FINAL += amt_of_cups_to_add

        # formatting
        print()

    def take(self):
        """ main code logic for collecting coffee machine's revenue """

        # global money_FINAL

        print('I gave you ${}'.format(self.money_FINAL))
        # update money to 0
        self.money_FINAL = 0
        # formatting
        print()

    def main(self):
        """ to run main code """

        # simulate the repeating loop to call for user's input
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()  # retrieve the action to operate
            print()  # leave a space for formatting

            # execute options
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining_menu()
            elif action == 'exit':
                exit()  # exit program
            else:  # exception case where user types in none of the above
                print('No menu found for option!')
                print()  # formatting

    # creates a representation for developers and debuggers
    # usually created first before the __str__ method
    # returns a string that is of a comprehensive description
    def __repr__(self):
        return f"water: {self.amt_of_water_FINAL}ml; " \
               f"milk: {self.amt_of_milk_FINAL}ml; " \
               f"coffee beans: {self.amt_of_beans_FINAL}g; " \
               f"cups: {self.amt_of_cups_FINAL}; " \
               f"amount of money: {self.money_FINAL}"

    # __str__ defines the behavior of the str() function
    # returns a string that is highly readable
    def __str__(self):
        return 'This is a standard licensed issued coffee machine'


'''
# test codes
coffee_machine = CoffeeMachine()
print('before:')
coffee_machine.remaining_menu()
print()
coffee_machine.buy()
print('after:')
coffee_machine.remaining_menu()
'''

coffee_machine = CoffeeMachine()
coffee_machine.main()
