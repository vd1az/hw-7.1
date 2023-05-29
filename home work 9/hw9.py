contact_book = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."
    return wrapper

@input_error
def add_contact(name, phone):
    contact_book[name] = phone
    return "Contact added successfully."

@input_error
def change_contact(name, phone):
    contact_book[name] = phone
    return "Contact updated successfully."

@input_error
def get_phone(name):
    return contact_book[name]

def show_all_contacts():
    if contact_book:
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

def main():
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            print("How can I help you?")
        
        elif command.startswith("add"):
            parts = command.split()
            if len(parts) == 3:
                _, name, phone = parts
                print(add_contact(name, phone))
            else:
                print("Invalid input. Please try again.")
        
        elif command.startswith("change"):
            parts = command.split()
            if len(parts) == 3:
                _, name, phone = parts
                print(change_contact(name, phone))
            else:
                print("Invalid input. Please try again.")
        
        elif command.startswith("phone"):
            parts = command.split()
            if len(parts) == 2:
                _, name = parts
                print(get_phone(name))
            else:
                print("Invalid input. Please try again.")
        
        elif command == "show all":
            show_all_contacts()
        
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
