import datetime
from Rent import get_datetime  # Import the get_datetime function from Rent module

def return_land(land_info, kitta_number, customer_name, duration, fine_rate):
    for land in land_info:
        if land[0] == kitta_number and land[-1] != 'Available':
            land[-1] = 'Available'

            # Calculate fine if return is late
            rented_time = datetime.datetime.strptime(land[-2], '%Y%m%d%H%M%S')
            current_time = datetime.datetime.strptime(get_datetime(), '%Y%m%d%H%M%S')
            duration_rented = (current_time - rented_time).days // 30
            fine = max(0, duration_rented - int(duration)) * fine_rate

            # Generate invoice
            current_time_str = get_datetime()
            invoice = f"Return_{kitta_number}_{customer_name}_{current_time_str}.txt"

            with open(invoice, 'w') as file:
                total_amount = int(land[3]) * int(duration) + fine
                file.write(f"Customer Name: {customer_name}\nKitta Number: {kitta_number}\nCity/District: {land[1]}\nLand Faced: {land[2]}\nDate and Time of Return: {current_time_str}\nDuration of Rent: {duration} months\nArea of Land (anna): {land[3]}\nFine Rate: {fine_rate} NPR\nFine Amount: {fine} NPR\nTotal Amount: {total_amount} NPR")

            print("Land returned successfully!")
            return

    print("Land not rented or invalid kitta number.")



# Function to apply fine for late returns
def apply_fine(land_info, fine_rate):
    for land in land_info:
        if land[-1] != 'Available':
            # Calculate duration since rented
            rented_time = get_datetime()
            rented_time_obj = datetime.datetime.strptime(rented_time, '%Y%m%d%H%M%S')
            duration = (rented_time_obj - datetime.datetime.strptime(land[-2], '%Y%m%d%H%M%S')).days // 30

            if duration >= 0:
                fine = fine_rate * duration
                total_amount = int(land[3]) * duration + fine

                # Update invoice with fine details
                invoice = f"Fine_{land[0]}_{rented_time}.txt"
                with open(invoice, 'w') as file:
                    file.write(f"Customer Name: {land[-3]}\nKitta Number: {land[0]}\nCity/District: {land[1]}\nLand Faced: {land[2]}\nDate and Time of Return: {rented_time}\nDate and Time of Rent: {land[-2]}\nDuration of Rent: {duration} months\nArea of Land (anna): {land[3]}\nFine Amount: {fine} NPR\nTotal Amount (including fine): {total_amount} NPR")

                print(f"Fine applied for kitta number {land[0]}: {fine} NPR")


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
