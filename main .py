import datetime
from Rent import read_land_info, display_lands, rent_land

def main():
    filename = "land_info.txt"
    land_info = read_land_info(filename)

    while True:
        print("\n1. Display Available and Unavailable Lands")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_lands(land_info)
        elif choice == '2':
            rent_multiple_lands(land_info)
        elif choice == '3':
            kitta_number = input("Enter kitta number of land to return: ")
            customer_name = input("Enter customer name: ")
            duration = input("Enter duration of rent (in months): ")
            try:
                rent_land(land_info, kitta_number, customer_name, duration)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    with open(filename, 'w') as file:
        for land in land_info:
            file.write(", ".join(land) + "\n")

def rent_multiple_lands(land_info):
    while True:
        kitta_number = input("Enter kitta number of land to rent (or 'q' to go back): ")
        if kitta_number.lower() == 'q':
            break
        if not kitta_number.isdigit():
            print("Invalid input. Kitta number must be a valid number.")
            continue
        customer_name = input("Enter customer name: ")
        if not customer_name.isalpha():
            print("Invalid input. Customer name must contain only alphabets.")
            continue
        duration = input("Enter duration of rent (in months): ")
        try:
            rent_land(land_info, kitta_number, customer_name, duration)
        except ValueError as e:
            print(f"Error renting land: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  

if __name__ == "__main__":
    main()
