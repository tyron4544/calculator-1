class BankAccountSystem:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account details

    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        password = input("Set your password: ")

        # Check if the account already exists
        if name in self.accounts:
            print("Account already exists. Please log in.")
            return

        # Create a new account with initial balance of 0
        self.accounts[name] = {
            'age': age,
            'password': password,
            'balance': 0
        }
        print(f"Account registered successfully for {name}!")

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name in self.accounts and self.accounts[name]['password'] == password:
            print("Login successful!")
            return name
        else:
            print("Login failed. Please check your name and password.")
            return None

    def deposit(self, account_name):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.accounts[account_name]['balance'] += amount
            print(f"Deposit successful! New balance: {self.accounts[account_name]['balance']}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, account_name):
        amount = float(input("Enter withdrawal amount: "))
        password = input("Enter your password: ")

        if password != self.accounts[account_name]['password']:
            print("Incorrect password. Withdrawal denied.")
            return

        if 0 < amount <= self.accounts[account_name]['balance']:
            self.accounts[account_name]['balance'] -= amount
            print(f"Withdrawal successful! New balance: {self.accounts[account_name]['balance']}")
        elif amount > self.accounts[account_name]['balance']:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def change_password(self, account_name):
        old_password = input("Enter your old password: ")
        if old_password == self.accounts[account_name]['password']:
            new_password = input("Enter your new password: ")
            self.accounts[account_name]['password'] = new_password
            print("Password changed successfully!")
        else:
            print("Incorrect old password. Password change failed.")

    def view_balance(self, account_name):
        password = input("Enter your password: ")
        if password == self.accounts[account_name]['password']:
            print(f"Current balance: {self.accounts[account_name]['balance']}")
        else:
            print("Incorrect password. Cannot view balance.")

    def menu(self):
        print("\n--- Bank Menu ---")
        print("""1. Deposit
2. Withdraw
3. Change Password
4. View Balance
5. Logout
6. Exit
""")

# Main execution loop
bnk = BankAccountSystem()

while True:
    action = input("\nEnter 1-Register or 2-Login: ")
    if action == '1':
        bnk.register()
    elif action == '2':
        account_name = bnk.login()
        if account_name:
            while True:
                bnk.menu()
                choice = input("Select an option: ")
                if choice == '1':
                    bnk.deposit(account_name)
                elif choice == '2':
                    bnk.withdraw(account_name)
                elif choice == '3':
                    bnk.change_password(account_name)
                elif choice == '4':
                    bnk.view_balance(account_name)
                elif choice == '5':
                    print("Logged out successfully.")
                    break  # Break out to the main menu
                elif choice == '6':
                    print("Exiting the system.")
                    exit()  # Exit the system
                else:
                    print("Invalid option. Please try again.")
    else:
        print("Invalid option. Please try again.")


