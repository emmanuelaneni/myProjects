# First function to add to a contact

def add_contact(contact):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")

    contact[name] = {"phone": phone, "email": email}

# View contacts 

def view_contact(contact):
    if not contact:
        print("No contact found.")
    else:
        for name, details in contact.items():
            print(f"'Name': {name}")
            print(f"'Phone': {details['phone']} ")
            print(f"'Phone': {details['email']} ")

#Search for a contact

def search_contact(contact):
    name = input("Enter the name of contact you want to search for: ")
    if name in contact:
        details = contact[name]
        print(f"'Name': {name}")
        print(f"'Phone': {details['phone']} ")
        print(f"'Phone': {details['email']} ")
    else:
        print(f"No contact registered for this name {name}")
    
# Deleting a contact

def delete_contact(contact):
    name = input("Enter the name of the contact to delete: ")
    if name in contact:
        del contact[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found for {name}.")

# To run the program

def main():
    contacts = {}  # This is our contact book
    
    while True:
        print("\nBasic Contact Book")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
