class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disp_cups = 9
        self.money = 550

    def buy(self, **products):
        def coffee_maker(water_, milk_, coffee_, money_):
            if water_ <= self.water and milk_ <= self.milk and coffee_ <= self.coffee_beans:
                print('I have enough resources, making you a coffee!\n')
                self.water -= water_
                self.milk -= milk_
                self.coffee_beans -= coffee_
                self.disp_cups -= 1
                self.money += money_
            else:
                if water_ > self.water:
                    print('Sorry, not enough water!\n')
                elif milk_ > self.milk:
                    print('Sorry, not enough milk!\n')
                elif coffee_ > self.coffee_beans:
                    print('Sorry, not enough coffee beans!\n')

        order = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')

        if order.isdigit():
            for i in products:
                if order == products[i]['val']:
                    coffee_maker(products[i]['water'], products[i]['milk'], products[i]['coffee'], products[i]['price'])
        elif order == 'back':
            pass

    def fill(self):
        self.water += int(input('\nWrite how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.disp_cups += int(input('Write how many disposable cups do you want to add:\n'))
        print('')

    def take(self):
        print(f'\nI gave you ${self.money}\n')
        self.money = 0

    def start(self, **products):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action == 'buy':
                self.buy(**products)
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                print(f'''\nThis coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.disp_cups} of disposable cups''')
                print(f'${self.money} of money' if self.money > 0 else '0 of money')
            elif action == 'exit':
                break


test_machine = CoffeeMachine()

test_machine.start(espresso={'val': '1', 'price': 4, 'water': 250, 'milk': 0, 'coffee': 16},
                   latte={'val': '2', 'price': 7, 'water': 350, 'milk': 75, 'coffee': 20},
                   cappuccino={'val': '3', 'price': 6, 'water': 200, 'milk': 100, 'coffee': 12})
