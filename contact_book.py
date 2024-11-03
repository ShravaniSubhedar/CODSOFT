class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts):
            print(f"{idx + 1}. {contact}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("Contact updated.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, updated_contact)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("Invalid input.")

        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
