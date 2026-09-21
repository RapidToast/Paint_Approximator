import json
import math

PRODUCT_FILE = "products.json"


# Default product information
default_products = {
    "Product 1": {
        "price": 35.00,
        "coverage": 300
    },

    "Product 2": {
        "price": 45.00,
        "coverage": 200
    },

    "Product 3": {
        "price": 55.00,
        "coverage": 150
    }
}


# Load saved product information
def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        save_products(default_products)
        return default_products.copy()


# Save product information
def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)


# Display current product information
def view_products(products):
    print("\n--- Current Product Information ---")

    for product, information in products.items():

        print(f"\n{product}")
        print(f"Price: ${information['price']:.2f} per gallon")
        print(f"Coverage: {information['coverage']} sq. ft. per gallon")


# Update price and coverage
def update_products(products):
    print("\n--- Update Products ---")

    for product, information in products.items():

        print(f"\n{product}")
        print("--------------------")
        print(f"Current Price: ${information['price']:.2f}")
        print(f"Current Coverage: {information['coverage']} sq. ft.")

        # Update price
        new_price = input(
            "Enter new price (press Enter to keep current): $"
        )

        if new_price != "":
            try:
                new_price = float(new_price)

                if new_price <= 0:
                    print("Price must be greater than 0.")

                else:
                    information["price"] = new_price

            except ValueError:
                print("Invalid price. Keeping current price.")

        # Update coverage
        new_coverage = input(
            "Enter new coverage (press Enter to keep current): "
        )

        if new_coverage != "":
            try:
                new_coverage = float(new_coverage)

                if new_coverage <= 0:
                    print("Coverage must be greater than 0.")

                else:
                    information["coverage"] = new_coverage

            except ValueError:
                print("Invalid coverage. Keeping current coverage.")

    save_products(products)

    print("\nProduct information saved successfully!")


# Create an estimate
def create_estimate(products):
    print("\n--- Create Paint Estimate ---")

    try:
        square_feet = float(
            input("How many square feet are you painting? ")
        )

        if square_feet <= 0:
            print("Square footage must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return


    print("\n================================")
    print("         PAINT ESTIMATE")
    print("================================")

    print(f"Job Size: {square_feet:,.2f} sq. ft.")


    for product, information in products.items():

        price = information["price"]
        coverage = information["coverage"]

        gallons_needed = math.ceil(
            square_feet / coverage
        )

        total_price = gallons_needed * price

        print(f"\n{product}")
        print("--------------------")
        print(f"Coverage: {coverage:,.0f} sq. ft./gallon")
        print(f"Gallons Needed: {gallons_needed}")
        print(f"Price Per Gallon: ${price:,.2f}")
        print(f"Estimated Cost: ${total_price:,.2f}")


    print("\n================================")


# Main menu
def main():

    products = load_products()

    while True:

        print("\n==============================")
        print("       PAINT ESTIMATOR")
        print("==============================")

        print("1. Create Paint Estimate")
        print("2. Update Products")
        print("3. View Product Information")
        print("4. Exit")

        choice = input("\nSelect an option: ")


        if choice == "1":
            create_estimate(products)

        elif choice == "2":
            update_products(products)

        elif choice == "3":
            view_products(products)

        elif choice == "4":
            print("\nThank you for using the Paint Estimator!")
            break

        else:
            print("\nInvalid selection. Please choose 1-4.")


main()
