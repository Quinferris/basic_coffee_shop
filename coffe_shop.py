
from datetime import time
import sys


print("   Welcome to the Coffee Shop!")
print('-' * 32)

total_order = 0
order_dict = {}


def Menu():
    menu1 = ("""
                C O F F E S H O P 24/7 M E N U

    a1 ~ Frappe..............$3    -----    b1 ~ Egg & Bacon Sandwhich.....$7
    a2 ~ Caramal Machiatto...$5    -----    b2 ~ Chocolate Cookie..........$2
    a3 ~ Espresso............$2    -----    b3 ~ Pop Cakes.................$1
    a4 ~ Water...............$1    -----    b4 ~ Crossant..................$3

    Please select the item number on the left to add to cart and recieve total

    """)
    return menu1


def order():
    ready_to_order = True
    while ready_to_order != False:
        ordering_q = input(
            """Do you know what you would like to order or do you need to see the menu?
                [M]enu or [R]eady to order or [Q]uit:   """)

        if ordering_q.upper() == "Q":
            sys.exit()
        elif ordering_q.upper() == "M":
            print(Menu())
        elif ordering_q.upper() == "R":
            ready_to_order = False
        else:
            print("Please enter valid letters only, try again.")
    print(" ")
    print(" ")

    add_cart = True
    while add_cart != False:
        order1 = input("What would you like to order?   ")
        if order1 == "Done":
            add_cart = False
            break
        elif order1 == 'a1':
            print("Frappe added to cart")
            global total_order
            total_order += 3
            drink_size()
            type_of_milk()
            special_instructions()
            order_dict['Frappe'] = (drink_sizes, milk_type, special_inst)
        elif order1 == 'a2':
            print('Caramal Machiatto added to cart')
            total_order += 5
            drink_size()
            type_of_milk()
            special_instructions()
            order_dict['Caramal Machiatto'] = (
                drink_sizes, milk_type, special_inst)
        elif order1 == 'a3':
            print('Espresso added to cart')
            total_order += 2
            drink_size()
            special_instructions()
            order_dict['Espresso'] = (drink_sizes, special_inst)
        elif order1 == 'a4':
            print('Water added to cart')
            total_order += 1
            drink_size()
            special_instructions()
            order_dict['Water'] = (drink_sizes, special_inst)
        elif order1 == 'b1':
            print("Bacon and Egg Sandwhich added to cart")
            total_order += 7
            temperature()
            special_instructions()
            order_dict['Bacon and Egg Sandwhich'] = (temp_food, special_inst)
        elif order1 == 'b2':
            print("Chocolate cookie added to cart")
            total_order += 2
            temperature()
            special_instructions()
            order_dict['Chocolate Cookie'] = (temp_food, special_inst)
        elif order1 == 'b3':
            print("Cake pop added to cart")
            total_order += 2
            special_instructions()
            order_dict['Cake pop'] = (special_inst)
        elif order1 == 'b4':
            print('Crossiant added to cart')
            total_order += 3
            temperature()
            special_instructions()
            order_dict['Crossiant'] = (temp_food, special_inst)
        # else:
        #     print("Please enter valid letters only, try again.")
    print(" ")
    print(" ")
    # print(order_dict)

    print("""       R E C I E P T
I T E M              INSTRUCTIONS""")
    for key, value in order_dict.items():
        print(key, '---->', value)
    print('')
    print(f'The Total Is ${total_order}')


def temperature():
    global temp_food
    temp_food = input("Do you want it warm or cold?     ")
    if temp_food.lower() == 'warm':
        return 'warm'
    elif temp_food.lower() == 'cold':
        return 'cold'


def drink_size():
    global drink_sizes
    drink_sizes = input("Wat size drink? [S]mall, [M]edium, [L]arge:     ")


def type_of_milk():
    global milk_type
    milk_type = input("What kind of milk? [A]lmond, [H]alf milk:     ")


def special_instructions():
    global special_inst
    special_inst = input("Any special instructions?     ")


def Checkout():
    pass


order()
