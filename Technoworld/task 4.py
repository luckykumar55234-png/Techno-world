import json

def signup():

    name = input("Enter name: ")
    if name.isalpha():
        print("Name Valid")
    else:
        print("Name Invalid")
        return

    age = int(input("Enter age: "))
    if age >= 18:
        print("Age Valid")
    else:
        print("Age Invalid")
        return

    email = input("Enter email: ")
    if "@" in email and "." in email:
        print("Email Valid")
    else:
        print("Email Invalid")
        return

    password = input("Enter password: ")
    if len(password) >= 6:
        print("Password Valid")
    else:
        print("Password must be 6 characters")
        return

    students = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Signup Successfully!")


def login():
    email = input("Enter email:")
    password = input("Enter password:")

    with open("student.json","r") as file:
        students = json.load(file)

    if email == students["email"] and password == students["password"]:

        print("Login successfuly")


def serach():

    email = input("Enter email to search")

    with open("student.json","r") as file:
        students = json.load(file)

    if email == students["email"]:

        print("Student found")
        print("Name:",students["name"])
        print("Age:",students["age"])
        print("Email:",students["email"])
    else:
        print("Student not Found")

def manu():
    while True:

        print("/n1.Signup")
        print("2.Login")
        print("3.Search")
        print("4.Exite")
        
        choice = input("Enter choice:")

        if choice == "1":
            signup()
        elif choice == "2":
             login()
        elif choice == "3":
            serach()
        elif choice == "4":
            print("Thank you")
            break
        else:
            print("Invalid chocie")

        
manu()           
            

    




    



    








    



        






    






    

     


    




    