
class Bankaccount:

    def __init__(self, name, AccountN, Balance):
        self.__ownername = name
        self.__accountnumber = AccountN
        self.___Balance = int(Balance)

    def Deposit(self, Balance):
        self.___Balance += Balance
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount <= self.___Balance:
            self.___Balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.___Balance

    def get_account_info(self):
        return self.__ownername, self.__accountnumber, self.___Balance


name = input("Enter your OwnerName: ")
AccountNumber = input("Enter your AccountNumber: ")
Balance = input("Enter your Balance: ")

ob = Bankaccount(name, AccountNumber, Balance)


def menu():

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Get Balance")
        print("4. Get Account Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            myamount = int(input("Enter your amount: "))
            ob.Deposit(myamount)

        elif choice == '2':
            myamount = int(input("Enter withdraw amount: "))
            ob.withdraw(myamount)

        elif choice == '3':
            print("Your Balance:", ob.get_balance())

        elif choice == '4':
            print("Account Info:", ob.get_account_info())

        elif choice == '5':
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


menu()


        

