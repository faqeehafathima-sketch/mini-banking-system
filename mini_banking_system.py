"""
Mini Banking System
A console-based Python OOP project demonstrating account management,
authentication, deposits, withdrawals, and transaction history.
"""

from datetime import datetime
import hashlib
import json
from pathlib import Path


DATA_FILE = Path("bank_data.json")


def hash_password(password):
    """Return a SHA-256 hash of a password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class BankAccount:
    """Represents one customer's bank account."""

    def __init__(self, username, password, balance=0.0, transactions=None):
        self.username = username
        self.password_hash = hash_password(password)
        self.balance = float(balance)
        self.transactions = transactions or []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Amount must be greater than zero."

        self.balance += amount
        self._record_transaction("Deposit", amount)
        return True, f"₹{amount:.2f} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Amount must be greater than zero."

        if amount > self.balance:
            return False, "Insufficient funds."

        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        return True, f"₹{amount:.2f} withdrawn successfully."

    def _record_transaction(self, transaction_type, amount):
        self.transactions.append({
            "type": transaction_type,
            "amount": round(amount, 2),
            "balance_after": round(self.balance, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_statement(self):
        if not self.transactions:
            return "No transactions yet."

        lines = ["\n--- Transaction History ---"]
        for item in self.transactions:
            lines.append(
                f"{item['timestamp']} | {item['type']:<10} | "
                f"₹{item['amount']:.2f} | Balance: ₹{item['balance_after']:.2f}"
            )
        return "\n".join(lines)


class BankSystem:
    """Manages users, authentication, persistence, and the active account."""

    def __init__(self):
        self.accounts = {}
        self.current_user = None
        self.load_data()

    def load_data(self):
        if not DATA_FILE.exists():
            return

        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            for username, details in data.items():
                account = BankAccount(
                    username,
                    "",
                    details.get("balance", 0),
                    details.get("transactions", [])
                )
                account.password_hash = details["password_hash"]
                self.accounts[username] = account
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Saved bank data could not be loaded.")

    def save_data(self):
        data = {}
        for username, account in self.accounts.items():
            data[username] = {
                "password_hash": account.password_hash,
                "balance": account.balance,
                "transactions": account.transactions
            }

        DATA_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")

    def register(self, username, password):
        if not username or not password:
            return False, "Username and password cannot be empty."

        if username in self.accounts:
            return False, "Username already exists."

        self.accounts[username] = BankAccount(username, password)
        self.save_data()
        return True, "Account created successfully."

    def login(self, username, password):
        account = self.accounts.get(username)

        if account and account.password_hash == hash_password(password):
            self.current_user = username
            return True, "Login successful."

        return False, "Invalid username or password."

    def logout(self):
        self.current_user = None

    def get_current_account(self):
        if self.current_user is None:
            return None
        return self.accounts[self.current_user]


def get_positive_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Enter an amount greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def account_menu(bank):
    while bank.current_user:
        account = bank.get_current_account()

        print("\n========== ACCOUNT MENU ==========")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            amount = get_positive_amount()
            _, message = account.deposit(amount)
            bank.save_data()
            print(message)

        elif choice == "2":
            amount = get_positive_amount()
            success, message = account.withdraw(amount)
            if success:
                bank.save_data()
            print(message)

        elif choice == "3":
            print(f"Current balance: ₹{account.balance:.2f}")

        elif choice == "4":
            print(account.get_statement())

        elif choice == "5":
            bank.logout()
            print("Logged out successfully.")

        else:
            print("Invalid option. Choose 1-5.")


def main():
    bank = BankSystem()

    while True:
        print("\n================================")
        print("       MINI BANKING SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Create username: ").strip()
            password = input("Create password: ")
            _, message = bank.register(username, password)
            print(message)

        elif choice == "2":
            username = input("Username: ").strip()
            password = input("Password: ")
            success, message = bank.login(username, password)
            print(message)

            if success:
                account_menu(bank)

        elif choice == "3":
            print("Thank you for using the Mini Banking System.")
            break

        else:
            print("Invalid option. Choose 1-3.")


if __name__ == "__main__":
    main()
