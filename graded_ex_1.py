# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}
cart = []

#Sorts the products by price in ascending or descending order.
def display_sorted_products(products_list, sort_order):
    if sort_order == "1" or sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "2" or sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    print("\nCategories:")
    for index, category in enumerate(products.keys(), start=1):
       print(f"{index}. {category}")
    return None
#Adds a product and quantity to the cart.
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))
    print(f"Added {quantity} x {product[0]} to the cart.")

def display_cart(cart):
    #display the contents of this cart
    print("\nYour Cart:")
    total_cost = sum(item[1] * item[2] for item in cart)
    for item in cart:
        product, price, quantity = item
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    #show the total cost of their shopping.
    print(f"Total cost: ${total_cost}")
    return total_cost

#Generates and displays the receipt.
def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
    for product, price, quantity in cart:  
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"\nTotal Cost: ${total_cost}")
    print(f"\nDelivery Address: {address}")
    print("\nYour items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email and " " not in email 

# Validate numeric input and range
def validate_numeric_input(prompt, valid_range=None):
    while True:
        value = input(prompt)  # input only takes one argument
        if value.isdigit() and (valid_range is None or 1 <= int(value) <= valid_range):
            return int(value)
        print(f"Invalid input! Please enter a number{' between 1 and ' + str(valid_range) if valid_range else ''}.")

#Shopping options loop
def shop_options(name, email, selected_category_items):
    while True:
        #After displaying the product details(display-products(products_list)), give user the option as follows
        print("\nOptions:")
        print("1. Select a product to buy")
        print("2. Sort the products according to the price")
        print("3. Go back to the category selection")
        print("4. Finish shopping\n")        
        option = validate_numeric_input("Please choose an option (1-4): ", 4)
        
        #1. Select a product to buy
        if option == 1:
            #ask the user to enter the number corresponding to the product
            product_number = validate_numeric_input("Enter the product number: ", len(selected_category_items))
            #ask the user to enter the quantity they want to buy
            quantity = validate_numeric_input(f"Enter the quantity for {selected_category_items[product_number - 1][0]}: ")
            add_to_cart(cart, selected_category_items[product_number - 1], quantity)
        
        #2. Sort the products according to the price
        elif option == 2:
            #ask the user if they want to sort ascending (1) or descending (2)
            while True:
                sort_order = ("\nSort by price: '1' for ascending, '2' for descending: ")
                if sort_order == "1" or sort_order == "2" or sort_order == "asc" or sort_order == "desc":
                    sorted_products = display_sorted_products(selected_category_items, sort_order)
                    break
                else:
                    print("Invalid input!")
            display_products(sorted_products)
        
        #3. Go back to the category selection
        elif option == 3:
            return  # Go back to category selection
        
        #4. Finish shopping
        elif option == 4:
            #Depending on whether the user ordered a product, the program will show do different things
            if cart:
                total_cost = display_cart(cart)
                #Ask them a delivery address.
                address = input("\nPlease enter your delivery address: ")
                #generate a receipt
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("\nThank you for using our portal. Hope you buy something from us next time. Have a nice day!")
            exit()  

def main():
    #ask the user their name. 
    name = input("Please enter your name(both first name and last name, only contain alphabets): ")
    #validate the name
    while not validate_name(name):
        name = input("The name is invalid! Please enter a valid name again: ")
    
    #ask the user their email address. 
    email = input("Please enter your email address: ")
    #validate the email address
    while not validate_email(email):
        email = input("The email is invalid! Please enter a valid email address again: ")
    
    while True:
        #show only the categories of products available for shopping
        display_categories()
        #Ask the user which category they would like to explore
        category_choice = validate_numeric_input("\nWhich category would you like to explore (enter the number): ", len(products))  
        #Once the user selects a category, the program should show all the products available under that category, including the price.
        selected_category = list(products.keys())[category_choice - 1]
        selected_category_items = products[selected_category]
        # Display the products in the selected category
        print(f"\nSelected Category: {selected_category}")
        display_products(selected_category_items)       
            
        # Proceed with shopping options
        shop_options(name, email, selected_category_items)

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
