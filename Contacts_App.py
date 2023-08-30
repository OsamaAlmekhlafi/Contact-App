# Done By: Osama Abdo Modhish
class Contact:

    # This function: Receives name, phone, and email.

    def __init__(self, name, phone, email):

        self.name = name
        self.phone = phone
        self.email = email

    # This Function Return a string representation of the contact details.
    def __str__(self):

        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    # Initialize a ContactManager object with an empty list of contacts.

    def __init__(self):

        self.contacts = []
       # This function: It receives an object from Contact and adds it to the contact list

    def add_contact(self, contact):

        self.contacts.append(contact)
    #  This function: Can Remove a contact from the list based on the name.

    def remove_contact(self, name):

        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break

    # This function: I Search for a contact in the list based on the name.
    # If the contact is found, it is returned.
    def search_contact(self, name):

        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    # This function: Displays all contacts in the list.
    # If no contacts found, it prints "No contacts found".

    def display_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts found")
        else:
            for contact in self.contacts:
                print(f"Your contact is :> {contact}")
                print("--------------------")


# Create a ContactManager object
contact_manager = ContactManager()

while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name of the contact to remove: ")
        contact_manager.remove_contact(name)
        print("Contact removed successfully!")

    elif choice == "3":
        name = input("Enter name of the contact to search: ")
        found_contact = contact_manager.search_contact(name)
        if found_contact:
            print("Contact found:")
            print(found_contact)
        else:
            print("Contact not found!")

    elif choice == "4":
        print("Contacts:")
        contact_manager.display_contacts()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
