import random  # Importing the random module to generate random numbers
from onlinebanking_system.hashing import hash_pin
from onlinebanking_system.interest import calculate_simple_interest, calculate_compound_interest


class BankingSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None  # Initialize logged_in_user to keep track of the logged-in user

    def hash_pin(self, pin, salt=None):
        if salt is None:
            salt = str(random.randint(1000, 9999))  # Generate a random salt if not provided
        return hash_pin(pin, salt), salt

    def register_user(self, username, pin):
        if username in self.users:
            print("Username already exists.")
            return False
        hashed_pin, salt = self.hash_pin(pin)
        self.users[username] = {'pin': hashed_pin, 'salt': salt, 'balance': 0}
        print(f"User {username} registered successfully.")
        return True

    def login(self, username, pin):
        if username not in self.users:
            print("Username not found.")
            return False

        user = self.users[username]
        hashed_pin, _ = self.hash_pin(pin, user['salt'])  # Hash the provided PIN with the stored salt

        if hashed_pin == user['pin']:
            self.logged_in_user = username
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN.")
            return False

    def set_security_question(self, question, answer):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        self.users[self.logged_in_user]['security_question'] = question
        self.users[self.logged_in_user]['security_answer'] = answer
        print("Security question set successfully.")

    def recover_pin(self, username):
        if username not in self.users:
            print("Username not found.")
            return

        user = self.users[username]
        if 'security_question' not in user or not user['security_question']:
            print("No security question set. Unable to recover PIN.")
            return

        print(f"Security Question: {user['security_question']}")
        answer = input("Your answer: ")
        if answer == user['security_answer']:
            new_pin = input("Enter new PIN: ")
            hashed_pin, salt = self.hash_pin(new_pin)
            user['pin'] = hashed_pin
            user['salt'] = salt
            print("PIN reset successful.")
        else:
            print("Incorrect answer. Unable to reset PIN.")

    def deposit(self, amount):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        self.users[self.logged_in_user]['balance'] += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if self.users[self.logged_in_user]['balance'] < amount:
            print("Insufficient funds.")
            return

        self.users[self.logged_in_user]['balance'] -= amount
        print(f"Withdrawn ${amount:.2f}")

    def transfer(self, recipient, amount):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if recipient not in self.users:
            print("Recipient not found.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if self.users[self.logged_in_user]['balance'] < amount:
            print("Insufficient funds.")
            return

        self.users[self.logged_in_user]['balance'] -= amount
        self.users[recipient]['balance'] += amount
        print(f"Transferred ${amount:.2f} to {recipient}")

    def check_balance(self):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        balance = self.users[self.logged_in_user]['balance']
        print(f"Your current balance is ${balance:.2f}")

    def logout(self):
        if not self.logged_in_user:
            print("No user is currently logged in.")
            return

        print(f"Logging out {self.logged_in_user}...")
        self.logged_in_user = None
        print("Logout successful.")
