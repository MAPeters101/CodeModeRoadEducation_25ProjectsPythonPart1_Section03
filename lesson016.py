print("Welcome to the Java Cafe\n")

price = 0
sizeCheckoutCoffee = "None"
sizeCheckoutCookies = "None"
sizeCheckoutCake = "None"

coffee = input("Would you like coffee? ")
if coffee.lower() == "yes":
    print("Sizes:\n1. Small: $3\n2. Medium: $5\n3. Large: $7\n")
    size_choice = int(input("What size would you like? "))
    if size_choice > 3 or size_choice < 1:
        print("You can't get coffee :(")
    else:
        if size_choice == 1:
            sizeCheckoutCoffee = "Small"
            price += 3
        elif size_choice == 2:
            sizeCheckoutCoffee = "Medium"
            price += 5
        elif size_choice == 3:
            sizeCheckoutCoffee = "Large"
            price += 7

cookies = input("Would you like cookies? ")
if cookies.lower() == "yes":
    print("Sizes:\n1. Small: $1\n2. Medium: $3\n3. Large: $5\n")
    size_choice = int(input("What size would you like? "))
    if size_choice > 3 or size_choice < 1:
        print("You can't get cookies :(")
    else:
        if size_choice == 1:
            sizeCheckoutCookies = "Small"
            price += 1
        elif size_choice == 2:
            sizeCheckoutCookies = "Medium"
            price += 3
        elif size_choice == 3:
            sizeCheckoutCookies = "Large"
            price += 5

cake = input("Would you like cake? ")
if cake.lower() == "yes":
    print("Sizes:\n1. Small: $5\n2. Medium: $10\n3. Large: $15\n")
    size_choice = int(input("What size would you like? "))
    if size_choice > 3 or size_choice < 1:
        print("You can't get cookies :(")
    else:
        if size_choice == 1:
            sizeCheckoutCake = "Small"
            price += 5
        elif size_choice == 2:
            sizeCheckoutCake = "Medium"
            price += 10
        elif size_choice == 3:
            sizeCheckoutCake = "Large"
            price += 15

print('---------------------------------')
print("Order summary: ")
print(f"Coffee size: {sizeCheckoutCoffee}")
print(f"Cookie size: {sizeCheckoutCookies}")
print(f"Cake size: {sizeCheckoutCake}")
print("Total: ${:.2f}".format(price))
