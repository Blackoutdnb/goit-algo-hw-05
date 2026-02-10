def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lower()
    return command, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Contact not found"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    _ = contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error    
def show_phone (args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts(args, contacts):
    if not contacts:
        return "No contacts."
    else:
        lines = []
        for name, phone in contacts.items():
            lines.append(f"{name}: {phone}")
        return "\n".join(lines)

def main():
    contacts = {}

    while True:
        user_input = input("").strip()
        if not user_input: continue
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()