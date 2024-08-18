from abc import ABC, abstractmethod
import pickle


class UserInterface(ABC):
    @abstractmethod
    def display_contact(self, contact):
        pass

    @abstractmethod
    def display_command_help(self):
        pass

    @abstractmethod
    def display_upcoming_birthdays(self, birthdays):
        pass
class ConsoleInterface(UserInterface):
    def display_contact(self, contact):
        print(f"Contact name: {contact.name.value}, phones: {'; '.join(p.value for p in contact.phones)}, birthday: {contact.birthday}")

    def display_command_help(self):
        print("Available commands:")
        print("add <name> <phone>")
        print("change <name> <old_phone> <new_phone>")
        print("phone <name>")
        print("all")
        print("add-birthday <name> <birthday>")
        print("show-birthday <name>")
        print("birthdays")
        print("close")

    def display_upcoming_birthdays(self, birthdays):
        if not len(birthdays):
            print("There are no upcoming birthdays.")
        else:
            for day in birthdays:
                print(f"Congratulations to {day['name']} on {day['congratulation_date']}")

def main():
    book = load_data()
    interface = ConsoleInterface()  # Вибір інтерфейсу

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)  # Збереження перед виходом з програми
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(book, args))

        elif command == "change":
            print(change_contact(book, args))

        elif command == "phone":
            contact = book.find(args[0])
            if contact:
                interface.display_contact(contact)
            else:
                raise KeyError

        elif command == "all":
            print(all_contact(book))

        elif command == "add-birthday":
            print(add_birthday(book, args))

        elif command == "show-birthday":
            contact = book.find(args[0])
            if contact:
                print(interface.display_contact(contact))
            else:
                raise KeyError

        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            interface.display_upcoming_birthdays(birthdays)

        else:
            interface.display_command_help()
