import datetime

def read_land_info(filename):
    land_info = []
    with open(filename, 'r') as file:
        for line in file:
            land_info.append(line.strip().split(', '))
    return land_info

# Function to display available and unavailable lands
def display_lands(land_info):
    print("Available Lands:")
    for land in land_info:
        if land[-1] == 'Available':
            print(", ".join(land))

    print("\nUnavailable Lands:")
    for land in land_info:
        if land[-1] != 'Available':
            print(", ".join(land))

# Function to rent land
def rent_land(land_info, kitta_number, customer_name, duration):
    for land in land_info:
        if land[0] == kitta_number and land[-1] == 'Available':
            land[-1] = 'Not Available'

            # Generate invoice
            current_time = get_datetime()
            invoice_filename = f"Invoice_{kitta_number}_{customer_name}_{current_time}.txt"
            with open(invoice_filename, 'w') as file:
                total_amount = int(land[3]) * int(duration)
                file.write(f"Customer Name: {customer_name}\nKitta Number: {kitta_number}\nCity/District: {land[1]}\nLand Faced: {land[2]}\nArea of Land (anna): {land[3]}\nDate and Time of Rent: {current_time}\nDuration of Rent: {duration} months\nTotal Amount: {total_amount} NPR")

            print("Land rented successfully!")
            return

    print("Land not available or invalid kitta number.")

# Function to display date and time
def get_datetime():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y%m%d%H%M%S")

def dates():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d/%m/%Y")
