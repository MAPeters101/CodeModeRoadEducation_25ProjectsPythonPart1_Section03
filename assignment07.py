price = 0
pizza_selected = "None"
topping_selected = "None"
drink_selected = "None"

print("Welcome to Pizza Paradise!\n")

print("\nAvailable Pizza Sizes:")
print("1. Small ($10) \n2. Medium ($15) \n3. Large ($20)")

#ask the user what size they want by typing in a certain number (HINT: wrap the input around an int() so that you can use the input variable as a number)
pizza_size = int(input("Please enter the size of pizza you would like: "))

#use an if statement to check if the size that the user entered is greater than 3 or less than 1
if pizza_size > 3 or pizza_size < 1:
    print("Invalid entry, you will not get a pizza.")
#inside of an else statement, you will increase the value of the price variable by 10 if the user entered 1, 15 if the user entered 2, and 20 if the user entered 3 for the size input
else:
    if pizza_size == 1:
        price += 10
        pizza_selected = "Small"
    elif pizza_size == 2:
        price += 15
        pizza_selected = "Medium"
    if pizza_size == 3:
        price += 20
        pizza_selected = "Large"

    print("\nAvailable Pizza Toppings:")
    print(
        "1. Pepperoni ($2) \n2. Mushrooms ($1.50) \n3. Onions ($1) \n4. Extra Cheese ($1.75)"
    )

    #ask the user what topping (ONLY ONE) they want by typing in a certain number (HINT: wrap the input around an int() so that you can use the input variable as a number)
    pizza_toppings = int(input("Please select ONLY 1 topping: "))
    #use an if statement to check if the topping that the user entered is greater than 4 or less than 1. This means that they selected a topping that was not in the menu.
    if pizza_toppings > 4 or pizza_toppings < 1:
        print("Invalid entry, you will not get any toppings.")
    #inside of an else statement, you will increase the value of the price variable by 2 if the user entered 1, 1.5 if the user entered 2, 1 if the user entered 3, and 1.75 if the user entered 4 for the topping input
    else:
        if pizza_toppings == 1:
            price += 2
            topping_selected = "Pepperoni"
        if pizza_toppings == 2:
            price += 1.5
            topping_selected = "Mushrooms"
        if pizza_toppings == 3:
            price += 1
            topping_selected = "Onions"
        if pizza_toppings == 4:
            price += 1.75
            topping_selected = "Extra Cheese"

print("\nAvailable Drinks:")
print("1. Soda ($2) \n2. Water ($1)")

#ask the user what drink they want by typing in a certain number (HINT: wrap the input around an int() so that you can use the input variable as a number)
drink = int(input("What drink would you like: "))
#use an if statement to check if the drink that the user entered is greater than 2 or less than 1. This means that they selected a drink that was not in the menu.
if drink > 2 or drink < 1:
    print("Invalid entry, you will not get a drink.")
#inside of an else statement, you will increase the value of the price variable by 2 if the user entered 1, and 1 if the user entered 1 for the drink input
else:
    if drink == 1:
        price += 2
        drink_selected = "Soda"
    elif drink == 2:
        price += 1
        drink_selected = "Water"


#this is the final part of the code. Notice how it is commented out. This is because I would like you to start getting the hang of writing your own final print statements and using the format keyword. Just retype the code below, so that you get practice writing output code.

#print("-------------------------------\n")
#print("Order Summary:")
#print(f"Pizza Size: {size_out}")
#print(f"Topping: {topping_out}")
#print(f"Drink: {drink_out}")
#print("Total Cost: ${:.2f}".format(price))

print("--------------------------------\n")
print("Order Summary:")
print(f"Pizza Size: {pizza_selected}")
print(f"Topping: {topping_selected}")
print(f"Drink: {drink_selected}")
print(f"Total Cost: ${price:.2f}")




