from src.bank import Bank
import threading
import time

def main():
    bank = Bank()

    while True:
        if not bank.get_current_user():
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose: ")
            if choice == '1':
                name = input("Name: ")
                email = input("Email: ")
                password = input("Password: ")
                if bank.register_user(name, email, password):
                    print("Registered successfully")
                else:
                    print("Registration failed")
            elif choice == '2':
                email = input("Email: ")
                password = input("Password: ")
                if bank.login(email, password):
                    print("Logged in")
                else:
                    print("Login failed")
            elif choice == '3':
                break
        else:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Balance")
            print("5. Transactions")
            print("6. Logout")
            choice = input("Choose: ")
            if choice == '1':
                amount = float(input("Amount: "))
                if bank.deposit(amount):
                    print("Deposited")
                else:
                    print("Failed")
            elif choice == '2':
                amount = float(input("Amount: "))
                if bank.withdraw(amount):
                    print("Withdrawn")
                else:
                    print("Failed")
            elif choice == '3':
                to_email = input("To email: ")
                amount = float(input("Amount: "))
                if bank.transfer(to_email, amount):
                    print("Transferred")
                else:
                    print("Failed")
            elif choice == '4':
                print(f"Balance: {bank.get_balance()}")
            elif choice == '5':
                transactions = bank.get_transactions()
                for t in transactions:
                    print(t)
            elif choice == '6':
                bank.logout()
                print("Logged out")

if __name__ == "__main__":
    # For real-time, perhaps run in thread, but for now, simple CLI
    main()