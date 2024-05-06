# task_4 - console bot v1.1

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Контакт не знайдено")
        except ValueError:
            print("Надайте необхідну кількість аргументів")
        except Exception as e:
            print(f"Непередбачувана помилка: {e}")
    return wrapper

def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

@input_error
def add_contact(contacts, name, phone):
    if not name or not phone:
        raise ValueError("Введіть ім'я та номер телефону, будь ласка.")
    contacts[name] = phone
    print(f"Контакт {name} додано з номером {phone}.")

@input_error
def change_contact(contacts, name, phone):
    if not name or not phone:
        raise ValueError("Введіть ім'я та номер телефону, будь ласка.")
    if name not in contacts:
        raise KeyError()
    contacts[name] = phone
    print(f"Номер телефону для {name} змінено на {phone}.")

@input_error
def show_phone(contacts, name):
    if not name:
        raise ValueError("Введіть ім'я, будь ласка.")
    if name not in contacts:
        raise KeyError()
    print(f"Номер {name}: {contacts[name]}")

@input_error
def show_all_contacts(contacts):
    if not contacts:
        print("Список контактів порожній.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

@input_error
def validate_command(command, args, valid_commands):
    if command not in valid_commands:
        raise ValueError("Невідома команда. Використовуйте: add, hello, change, phone, all, exit.")
    if command in ['add', 'change'] and len(args) < 2:
        raise ValueError("Введіть ім'я та номер телефону.")
    if command == 'phone' and len(args) < 1:
        raise ValueError("Введіть ім'я для пошуку.")
    if command == 'all' and args:
        raise ValueError("Команда 'all' не повинна мати аргументів.")

def main():
    contacts = {}
    print("Введіть команду (add, hello, change, phone, all, exit):")
    valid_commands = {'add', 'hello', 'change', 'phone', 'all', 'exit', 'close'}
    
    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)
        try:
            validate_command(command, args, valid_commands)
        except ValueError as ve:
            print(ve)
            continue

        if command == 'exit' or command == 'close':
            print("Програма завершує роботу.")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            add_contact(contacts, *args)
        elif command == 'change':
            change_contact(contacts, *args)
        elif command == 'phone':
            show_phone(contacts, *args)
        elif command == 'all':
            show_all_contacts(contacts)


if __name__ == '__main__':
    main()