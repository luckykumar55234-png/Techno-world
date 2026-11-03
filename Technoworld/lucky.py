
import json

def load_contacts():
    try:
        with open("student.json", "r") as file:
            return json.load(file)
    except:
        return {}


def save_contacts(contacts):
    with open("student.json", "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            name = input("Enter name: ")

            if not name.replace(" ", "").isalpha():
                print("Invalid Name!")
            else:
                break

        while True:
            phone = input("Enter phone: ")

            if not phone.isdigit() or len(phone) != 10:
                print("Invalid Phone! Enter 10 digits.")
            elif phone in contacts:
                print("Phone Already Exists!")
            else:
                break

        while True:
            email = input("Enter email: ")

            if "@" in email and "." in email:
                break
            else:
                print("Invalid Email!")

        contacts[phone] = {
            "name": name,
            "phone": phone,
            "email": email
        }

        save_contacts(contacts)
        print("Contact Added Successfully!")

    elif choice == "2":

        if contacts:
            for phone, contact in contacts.items():
                print(contact)
        else:
            print("No Contacts Found!")

    elif choice == "3":

        phone = input("Enter phone to search: ")

        if phone in contacts:
            print(contacts[phone])
        else:
            print("Contact Not Found!")

    elif choice == "4":

        phone = input("Enter phone to update: ")

        if phone in contacts:

            while True:
                name = input("Enter new name: ")

                if not name.replace(" ", "").isalpha():
                    print("Invalid Name!")
                else:
                    break

            while True:
                email = input("Enter new email: ")

                if "@" in email and "." in email:
                    break
                else:
                    print("Invalid Email!")

            contacts[phone]["name"] = name
            contacts[phone]["email"] = email

            save_contacts(contacts)
            print("Contact Updated Successfully!")

        else:
            print("Contact Not Found!")

    elif choice == "5":

        phone = input("Enter phone to delete: ")

        if phone in contacts:
            del contacts[phone]

            save_contacts(contacts)
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")




