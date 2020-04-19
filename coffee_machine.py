water = 400
milk = 540
coffee_beans = 120
disp_cups = 9
money = 550


def buy():
    def coffee_maker(water_, milk_, coffee_, money_):
        global water, milk, coffee_beans, disp_cups, money
        if water_ <= water and milk_ <= milk and coffee_beans <= coffee_beans:
            print('I have enough resources, making you a coffee!\n')
            water -= water_
            milk -= milk_
            coffee_beans -= coffee_
            disp_cups -= 1
            money += money_
        else:
            if water_ > water:
                print('Sorry, not enough water!\n')
            elif milk_ > milk:
                print('Sorry, not enough milk!\n')
            elif coffee_ > coffee_beans:
                print('Sorry, not enough coffee beans!\n')

    order = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')

    if order == '1':
        coffee_maker(250, 0, 16, 4)
    elif order == '2':
        coffee_maker(350, 75, 20, 7)
    elif order == '3':
        coffee_maker(200, 100, 12, 6)
    elif order == 'back':
        pass


def fill():
    global water, milk, coffee_beans, disp_cups, money
    water += int(input('\nWrite how many ml of water do you want to add:\n'))
    milk += int(input('Write how many ml of milk do you want to add:\n'))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    disp_cups += int(input('Write how many disposable cups do you want to add:\n'))
    print('')


def take():
    global money

    print(f'\nI gave you ${money}\n')
    money = 0


while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        print(f'''\nThis coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disp_cups} of disposable cups''')
        print(f'${money} of money' if money > 0 else '0 of money')
    elif action == 'exit':
        break
