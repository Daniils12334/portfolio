import hashlib
import random

class User:
    def __init__(self, login, password, name, age, balance):
        self.login = login
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.name = name
        self.age = age
        self.balance = balance

    def authenticate(self):
        """Ask user for login and password to authenticate"""
        login_input = input('Enter your login: ')
        password_input = hashlib.sha256(input('Enter your password: ').encode()).hexdigest()

        if login_input == self.login and password_input == self.password:
            print(f"Welcome, {self.name}!")
            return True
        else:
            print("Invalid login or password.")
            return False

    def withdraw(self):
        """Withdraw money from balance after password confirmation"""
        password_input = hashlib.sha256(input('Enter your password: ').encode()).hexdigest()
        if password_input != self.password:
            print("Incorrect password.")
            return

        withdraw_amount = int(input("Enter money you would like to withdraw: "))
        if withdraw_amount > self.balance:
            print(f"Not enough money, your current balance: {self.balance}$")
        else:
            self.balance -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}$. Your new balance is {self.balance}$")

    def deposit(self):
        """Deposit money into balance"""
        deposit_amount = int(input("Enter money you would like to deposit: "))
        self.balance += deposit_amount
        print(f'Your deposit is: {deposit_amount}, your balance now is {self.balance}')

    def status(self):
        """Print user details"""
        print(f'Your name is {self.name}, you are {self.age} years old, your current balance is {self.balance}$')

    def main(self):
        """Main loop to interact with user"""
        if not self.authenticate():  # Check if authentication is successful
            return
        
        while True:
            user_input = input('Enter operation type: 1-status 2-withdraw 3-deposit 4-exit: ')
            match user_input:
                case "1":
                    self.status()
                case "2":
                    self.withdraw()
                case "3":
                    self.deposit()
                case "4":
                    print(f'Goodbye {self.name}!')
                    break
                case _:
                    print("Invalid option, please try again.")


user1 = User("dan_bar", "run_nigga_run", "Daniils", 25, 5000)  # Creating a user with initial balance
user2 = User("deniss_zura", "den.zura.1234", "Deniss", 17, 2)  # Creating a user with initial balance

# user2.main()  # Running the banking system

user = input('enter your login')
match user:
    case "dan_bar":
        user1.main()
    case "deniss_zura":
        user2.main()
