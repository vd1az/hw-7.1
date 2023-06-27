import pickle

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.contacts = pickle.load(file)

    def search_contacts(self, search_string):
        matching_contacts = []
        for contact in self.contacts:
            if (
                search_string.lower() in contact.name.lower() or
                search_string in contact.phone_number
            ):
                matching_contacts.append(contact)
        return matching_contacts



address_book = AddressBook()

contact1 = Contact("John Doe", "123456789")
contact2 = Contact("Jane Smith", "987654321")
address_book.add_contact(contact1)
address_book.add_contact(contact2)

address_book.save_to_file("address_book.dat")

new_address_book = AddressBook()

new_address_book.load_from_file("address_book.dat")

search_string = "John"
matching_contacts = new_address_book.search_contacts(search_string)

for contact in matching_contacts:
    print("Name:", contact.name)
    print("Phone number:", contact.phone_number)
    print()
