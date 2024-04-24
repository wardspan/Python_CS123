import pickle

# Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should display a menu that lets the user look up a person’s email address, add a new name and email address, change an existing email address, and delete an existing name and email address. The program should pickle the dictionary and save it to a file when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.

def load_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_data(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def display_menu():
    print("1. Look up email address")
    print("2. Add new name and email address")
    print("3. Change existing email address")
    print("4. Delete name and email address")
    print("5. Exit")

def lookup_email(data):
    name = input("Enter the name: ")
    if name in data:
        print(f"Email address: {data[name]}")
    else:
        print("Name not found.")

def add_name_email(data):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    data[name] = email
    print("Name and email address added.")

def change_email(data):
    name = input("Enter the name: ")
    if name in data:
        email = input("Enter the new email address: ")
        data[name] = email
        print("Email address updated.")
    else:
        print("Name not found.")

def delete_name_email(data):
    name = input("Enter the name: ")
    if name in data:
        del data[name]
        print("Name and email address deleted.")
    else:
        print("Name not found.")

def main():
    file_path = '/Users/wardspan/Code/Python_CS123/Chapter9/8_name_email.pickle'
    data = load_data(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lookup_email(data)
        elif choice == '2':
            add_name_email(data)
        elif choice == '3':
            change_email(data)
        elif choice == '4':
            delete_name_email(data)
        elif choice == '5':
            save_data(data, file_path)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()