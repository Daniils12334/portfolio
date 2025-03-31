import hashlib
import json

USER_FILE = "bank_users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

class User:
    def __init__(self, login, password, name, age, balance):
        self.login = login
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.name = name
        self.age = age
        self.balance = balance

    def authenticate(self):
        password_input = hashlib.sha256(input('Enter your password: ').encode()).hexdigest()
        if password_input == self.password:
            print(f"Welcome, {self.name}!")
            return True
        else:
            print("Invalid password.")
            return False

    def withdraw(self):
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
            users[self.login]["balance"] = self.balance 
            save_users(users)  

    def deposit(self):

        deposit_amount = int(input("Enter money you would like to deposit: "))
        self.balance += deposit_amount
        print(f'Your deposit is: {deposit_amount}, your balance now is {self.balance}$')
        users[self.login]["balance"] = self.balance  
        save_users(users) 

    def status(self):

        print(f'Your name is {self.name}, you are {self.age} years old, your current balance is {self.balance}$')

    def main(self):

        if not self.authenticate():
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

def register():

    login = input("Enter new login: ")
    if login in users:
        print("User already exists!")
        return

    password = input("Enter new password: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    balance = float(input("Enter initial balance: "))

    new_user = User(login, password, name, age, balance)
    users[login] = new_user.__dict__  
    save_users(users)  

    print("User registered successfully!")


users = load_users()


while True:
    action = input("Do you want to (1) Register or (2) Login? (3) Exit: ")

    if action == "1":
        register()
    elif action == "2":
        user_login = input("Enter your login: ")
        if user_login in users:
            user_data = users[user_login]
            current_user = User(
                user_login,
                password=user_data["password"], 
                name=user_data["name"],
                age=user_data["age"],
                balance=user_data["balance"]
            )
            current_user.main()
        else:
            print("User not found.")
    elif action == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid option, please try again.")
