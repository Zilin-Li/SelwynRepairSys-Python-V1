# ============== Selwyn Panel Beaters MAIN PROGRAM ==============
# Student Name: Zilin Li
# Student ID : 1159924
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import spb_data    # spb_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We areusing date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line
# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = spb_data.col_customers
db_customers = spb_data.db_customers
col_services = spb_data.col_services
db_services = spb_data.db_services
col_parts = spb_data.col_parts
db_parts = spb_data.db_parts
#col_bills is useful for displaying the headings when listing bills
col_bills = spb_data.col_bills


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output

def list_parts():
    # List the ID, name, cost of all parts in alphabetical order
   
    # Convert the dictionary data into a list that displays the required data fields
    display_list = []
    
    # Iterate over all the parts in the dictionary and append them to the display list
    for part in db_parts.keys():
        display_list.append((part,
                             db_parts[part][0],
                             db_parts[part][1]))

    # Sort the display list by the name of the part (second element of each tuple)
    display_list.sort(key=lambda x: x[1])

    format_columns = "{: >4} | {: <15} | {: <12} "
    print("\nPart LIST\n")  # Display a heading for the output
    column_output(display_list, col_parts, format_columns)  # Call column_output function to display

    input("\nPress Enter to continue.")  # Pause to allow the user to see the output

def list_services():
    # List the ID, name, cost of all services in alphabetical order
    
    display_list = []
    
    # Iterate over all the services in the dictionary and append them to the display list
    for service in db_services.keys():
        display_list.append((service,
                             db_services[service][0],
                             db_services[service][1]))

    # Sort the display list by the name of the service (second element of each tuple)
    display_list.sort(key=lambda x: x[1])

    format_columns = "{: >4} | {: <22} | {: <12} "
    print("\nService LIST\n")  # Display a heading for the output
    column_output(display_list, col_services, format_columns)  # Call column_output function to display

    input("\nPress Enter to continue.")  # Pause to allow the user to see the output


def add_customer():
    while True:
        print("\n== Add Customer ==")
        while True:
            name = input("\nEnter customer's name: ").strip()
            if name=='':
                print("Customer name can not be empty")
                continue
            else:
                break
        
        while True:
            phone_number = input("Enter customer's phone number: ")
    
            # Verify that the phone number is in numeric form
            if not phone_number.isdigit():
                print("Invalid phone number. Please enter a valid phone number.")
                continue
            else:
                break
    
        while True:
            email = input("Enter customer's email address: ")

        # Verify that the email format is correct
            if "@" not in email:
                print("Invalid email address. Please enter a valid email address.")
                continue
            else:
                break
    
        # Get the next customer ID
        new_customer_id = next_id(db_customers)
    
        # Put the new customer data to database
        db_customers[new_customer_id] = {
            'details': [name, phone_number, email],
            'jobs': {}
        }
    
        print(f"\nCustomer {name} added successfully with ID {new_customer_id}.")
        # print(db_customers)

        # Ask user whether to add a new customer. 
        # If Y is selected, continue to add new customer's infomation. 
        # Select N to return to the main screen
        while True:
            choice = input("Do you want to add another customer? (Y/N): ").upper()
            if choice == 'N':
                return  # Return to the main menu
            elif choice == 'Y':
                break
            else:
                print("Invalid choice. Please enter Y for Yes or N for No.")


def add_job():
    # Loop to select a valid customer ID or exit to main menu
    while True:
        list_customers()  # Display all customers
        customer_id = input("Enter the customer ID to add job for, or 'X' to exit: ")

        # Exit the function if the user chooses to exit to the main menu
        if customer_id.upper() == 'X':
            return

        # Check if the entered customer ID is valid
        if customer_id.isdigit() and int(customer_id) in db_customers:
            customer_id = int(customer_id)
            break
        else:
            print("Invalid Customer ID. Please try again.")

    # Initialize lists to store selected services and parts, and a variable for total cost
    selected_services = []
    selected_parts = []
    total_cost = 0.0

    # Main loop for adding services or parts to the job
    while True:
        print("\nOptions for adding to job:")
        print(" 1 - Add Service")
        print(" 2 - Add Part")
        print(" 3 - Finish and Review Bill")
        choice = input("Enter your choice: ").upper()

        # Handling addition of services or parts
        if choice in ['1', '2']:
            while True:
                # Add service or part based on the user's choice
                if choice == '1':
                    list_services()
                    option_id = input("Enter the Service ID to add, or 'B' to go back: ")
                    db_option = db_services
                else:
                    list_parts()
                    option_id = input("Enter the Part ID to add, or 'B' to go back: ")
                    db_option = db_parts

                # Allow the user to go back to the previous menu
                if option_id.upper() == 'B':
                    break
                # Validate the selected service or part ID and add it to the job
                if option_id.isdigit() and int(option_id) in db_option:
                    option_id = int(option_id)
                    if choice == '1':
                        selected_services.append(option_id)
                    else:
                        selected_parts.append(option_id)
                    total_cost += db_option[option_id][1]
                    total_cost = round(total_cost, 2)  # Round the total cost to 2 decimal places
                    
                    print(f"Added {db_option[option_id][0]} to the job.")

                    # Ask the user if they want to continue adding items
                    continue_adding = input("Do you want to continue adding items? (Y/N): ").upper()
                    if continue_adding == 'N':
                        break
                else:
                    print("Invalid ID. Please try again.")

        # Handle the completion and review of the bill
        elif choice == '3':
            if not selected_services and not selected_parts:
                print("No services or parts added. Exiting to main menu.")
                return

            # Display bill details
            print_bill(customer_id, selected_services, selected_parts, total_cost)

            # Confirm the addition of the job
            confirm = input("\nConfirm job addition? (Y/N): ").upper()
            if confirm == 'Y':
                job_date = datetime.date.today()
                db_customers[customer_id]['jobs'][job_date] =[tuple(selected_services), tuple(selected_parts), total_cost, False]
                print("Job added successfully.")
            else:
                print("Job addition cancelled.")

            return

# Function to print the bill details
def print_bill(customer_id, selected_services, selected_parts, total_cost):
    print(f"\nClient name: {db_customers[customer_id]['details'][0]}")
    print("Job details:")
    print(f"  Date: {datetime.date.today()}")
    print("--------------------------------------------------")
    if selected_services:
        print("  Services:")
        print("  ID | Name                      |        Cost")
        for sid in selected_services:
            print(f"  {sid} | {db_services[sid][0]:<25} | {db_services[sid][1]:>10.2f}")
    if selected_parts:
        print("--------------------------------------------------")
        print("  Parts:")
        print("  ID | Name                      |        Cost")
        for pid in selected_parts:
            print(f"  {pid} | {db_parts[pid][0]:<25} | {db_parts[pid][1]:>10.2f}")
    print("--------------------------------------------------")
    print(f"  Total Cost: {total_cost:.2f}")


def bills_to_pay():
    # Display a heading for the output
    print("\nOutstanding Bills\n")

    # Initialize an empty list to store the display data
    display_list = []

    # Iterate over all customers in the database
    for customer_id, customer_data in db_customers.items():
        customer_name = customer_data['details'][0]
        customer_phone = customer_data['details'][1]

        # Check each job for the customer
        for job_date, job_details in customer_data['jobs'].items():
            # Check if the bill is unpaid
            if not job_details[3]:  # The 4th element in job_details is the payment status
                amount_due = job_details[2]  # The 3rd element in job_details is the amount
                # Append the data to the display list
                display_list.append((customer_name, customer_phone, job_date, amount_due))

    # Define the format for the columns
    format_columns = "{: <15} | {: <12} | {: <10} | {: >10}"

    # Use column_output function to display the data
    column_output(display_list, col_bills, format_columns)

    input("\nPress Enter to continue.")  # Pause to allow the user to see the output


def pay_bill():
    while True:
        # display all the customers with their ID, name, bill date
        print("\nCustomers:\n")
        for customer_id, customer_data in db_customers.items():
            print(f"ID: {customer_id}, Name: {customer_data['details'][0]}")

        # choose a customer with ID, or enter "X" to the main menu
        selected_customer_id = input("\nEnter the ID of the customer to pay bill, or enter 'X' to exit: ")
        if selected_customer_id.upper() == 'X':
            return  # return to main menu

        try:
            
            selected_customer_id = int(selected_customer_id)
            # Verify the customer id
            if selected_customer_id not in db_customers:
                print("Invalid Customer ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid ID or 'X' to exit.")
            continue

        # display the unpaid bill
        unpaid_bills = show_unpaid_bills(selected_customer_id)
        if not unpaid_bills:
            print("No unpaid bills for this customer.")
            choice = input("Enter 'B' to go back, or any other key to exit to main menu: ").upper()
            if choice == 'B':
                continue  # return the customer list
            else:
                return  # return to the main menu

        # Deal with the unpaid bill
        while True:
            # Enter the bill date to choose pay the bill,or not
            # Enter "B", back to customer list
            # Enter "X", back to main menu
            print (db_customers)
            bill_date_input = input("\nEnter the date of the bill to pay (YYYY-MM-DD), 'B' to go back, or 'X' to exit: ")
            if bill_date_input.upper() == 'B':
                break  
            if bill_date_input.upper() == 'X':
                return  

            try:
                bill_date = datetime.datetime.strptime(bill_date_input, '%Y-%m-%d').date()
                if bill_date not in unpaid_bills:
                    print("No unpaid bill for this date. Please try again.")
                    continue
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

            # Comfirm to pay
            confirm = input(f"Are you sure you want to mark the bill dated {bill_date} as paid? (Y/N): ").upper()
            if confirm == 'Y':
                db_customers[selected_customer_id]['jobs'][bill_date][3] = True
                print(f"Bill dated {bill_date} has been marked as paid.")
                unpaid_bills.remove(bill_date)
                if not unpaid_bills:
                    print("No more unpaid bills for this customer.")
                    input("Press any key to go back to main menu: ")
                    return

                next_action = input("Enter 'C' to continue paying, 'B' to select another customer, or 'X' to exit: ").upper()
                if next_action == 'C':
                    # Enter "C", show the updated unpaid bill list, until the user pay all the bill.
                    unpaid_bills = show_unpaid_bills(selected_customer_id)
                    continue
                elif next_action == 'B':
                    break  # return to customer list
                else:
                    return  # return to main menu
            elif confirm == 'N':
                print("Payment cancelled.")
                continue 
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                continue
            
# This function is use to display the unpaid bills for a specified customer.
def show_unpaid_bills(customer_id):
    
    print("\nUnpaid Bills:\n")
    unpaid_bills = []
    for job_date, job_details in db_customers[customer_id]['jobs'].items():
        if not job_details[3]: 
            print(f"Date: {job_date}, Amount: {job_details[2]}")
            unpaid_bills.append(job_date)
    return unpaid_bills



# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN PANEL BEATERS ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Parts")
    print(" 4 - Add Customer")
    print(" 5 - Add Job")
    print(" 6 - Display Unpaid Bills")
    print(" 7 - Pay Bill")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response != "X" and response != "x":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_parts()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_job()
    elif response == "6":
        bills_to_pay()
    elif response == "7":
        pay_bill()
    else:
        print("\n***Invalid response, please try again (enter 1-6 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Panel Beaters! ===\n")
