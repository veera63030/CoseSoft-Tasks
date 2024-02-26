# Install TinyDB using pip install tinydb

from tinydb import TinyDB, Query

# Initialize the database
db = TinyDB("contacts.json")
Contact = Query()

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")

    db.insert({"name": name, "phone": phone, "email": email})
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    contacts = db.all()
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_term = input("Enter search term: ")
    results = db.search(Contact.name.search(search_term))
    if not results:
        print(f"No contacts found for '{search_term}'.")
    else:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
