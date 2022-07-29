# Print Report
# Check Resources sufficient
# Process coins.
# Check transaction success

#Latte: 50ml Water
from xmlrpc.client import FastParser
from pyrsistent import get_in


water_source = float(500)
milk_source = float(400)
coffee_source = float(300)
money_source = 0


def print_report():

    print("Water: {w} ml".format(w = water_source))
    print("Milk: {m} ml".format(m = milk_source))
    print("Coffee: {c} gr".format(c = coffee_source))
    print("Money: ${mo}".format(mo=money_source))




coffee_type = {
    'Espresso':{
        'Water': float(50),
        'Coffee': float(18),
        'Milk': float(0),
        'Price': float(1.50)      
    },
    'Latte':{
        'Water': float(200),
        'Coffee': float(24),
        'Milk': float(150),
        'Price': float(2.50)       
    },
    'Cappucino':{
        'Water': float(250),
        'Coffee': float(24),
        'Milk': float(100),
        'Price': float(3.0)       
    }
}

isOn = True

def check_sufficient(coffee):
    error_message = ""
    is_sufficient = True
    if water_source < coffee_type[coffee]['Water']:
        error_message = "Sorry There is not enough water"
        print(error_message)
        is_sufficient = False
    elif coffee_source < coffee_type[coffee]['Coffee']:
        error_message = "Sorry there is not enough coffee."
        print(error_message)
        is_sufficient = False
    elif milk_source < coffee_type[coffee]['Milk']:
        is_sufficient = False
        print(error_message)
        error_message = "Sorry there is not enough milk."

    return is_sufficient

def insert_coin():
    get_quarters = float(input("How many quarters?: "))
    get_dimes = float(input("How many dimes?: "))
    get_nickels = float(input("How many nickels?: "))
    get_penny = float(input("How many pennies?: "))

    penny = 0.01 * get_penny
    quarter = 0.25 * get_quarters
    nickel = 0.05 * get_nickels
    dime = 0.10 * get_dimes

    total = penny + quarter + nickel + dime
    return total

# print(check_sufficient('Cappucino'))

def buy_espresso():
    print(coffee_type['Espresso'])

def buy_latte():
    print(coffee_type['Latte'])    

def buy_cappucino():
    print(coffee_type['Cappucino'])


while isOn: 
    get_input = input("What you like? (espresso/latte/cappucino): ")
    if get_input == "report":
        print_report()
        
    if get_input == "off":
        isOn = False

    if get_input == 'Espresso':
        buy_espresso()
        result = check_sufficient(get_input)
        if result == False:
            print(result)
        else:
            coin_inserted = insert_coin()

        if coin_inserted < coffee_type[get_input]['Price']:
            print("You inserted {m} Not enough money, here is the return".format(m = coin_inserted))
            isTryAgain = input('You want to try again?: ')
            if isTryAgain == 'no':
                isOn = False
        else:
            money_source += coffee_type[get_input]['Price']
            coffee_source -= coffee_type[get_input]['Coffee']
            water_source -= coffee_type[get_input]['Water']
            milk_source -= coffee_type[get_input]['Milk']

            change_money =  coin_inserted - coffee_type[get_input]['Price']
            change_money_format = "{:.2f}".format(change_money)
            print("You insert ${inserted:.2f}, Here is your change: ${c}".format(inserted = coin_inserted, c=change_money_format))
            print("Enjoy your {coffee_out}".format(coffee_out = get_input))
            isTryAgain = input('You want to buy some more coffee?: ')
            if isTryAgain == 'no':
                isOn = False        

    if get_input == 'Latte':
        buy_latte()

        result = check_sufficient(get_input)
        if result == False:
            print(result)
        
        else:
            coin_inserted = insert_coin()

        if coin_inserted < coffee_type[get_input]['Price']:
            print("You inserted {m} Not enough money, here is the return,".format(m = coin_inserted))
            isTryAgain = input('You want to try again?: ')
            if isTryAgain == 'no':
                isOn = False
        else:
            money_source += coffee_type[get_input]['Price']
            coffee_source -= coffee_type[get_input]['Coffee']
            water_source -= coffee_type[get_input]['Water']
            milk_source -= coffee_type[get_input]['Milk']

            change_money =  coin_inserted - coffee_type[get_input]['Price']
            change_money_format = "{:.2f}".format(change_money)
            print("You insert ${inserted:.2f}, Here is your change: ${c}".format(inserted = coin_inserted, c=change_money_format))
            print("Enjoy your {coffee_out}".format(coffee_out = get_input))
            isTryAgain = input('You want to buy some more coffee?: ')
            if isTryAgain == 'no':
                isOn = False        

    if get_input == 'Cappucino':
        buy_cappucino()

        result = check_sufficient(get_input)

        if result == False:
            print(result)
        else:
            coin_inserted = insert_coin()

        if coin_inserted < coffee_type[get_input]['Price']:
            print("You inserted {m} Not enough money, here is the return".format(m = coin_inserted))
            isTryAgain = input('You want to try again?: ')
            if isTryAgain == 'no':
                isOn = False     
        else:
            money_source += coffee_type[get_input]['Price']
            coffee_source -= coffee_type[get_input]['Coffee']
            water_source -= coffee_type[get_input]['Water']
            milk_source -= coffee_type[get_input]['Milk']

            change_money =  coin_inserted - coffee_type[get_input]['Price']
            change_money_format = "{:.2f}".format(change_money)
            print("You insert ${inserted:.2f}, Here is your change: ${c}".format(inserted = coin_inserted, c=change_money_format))
            print("Enjoy your {coffee_out}".format(coffee_out = get_input))
            isTryAgain = input('You want to buy some more coffee?: ')
            if isTryAgain == 'no':
                isOn = False                 
