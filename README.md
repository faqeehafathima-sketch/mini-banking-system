# Mini Banking System

A console-based banking simulation built with Python and Object-Oriented Programming.

This is a learning project that combines account management, login, deposits, withdrawals, transaction history, validation, and local data storage.

## Features

- Create an account
- Login with a username and password
- Store passwords as SHA-256 hashes
- Deposit money
- Withdraw money
- Check the current balance
- Prevent withdrawals above the available balance
- Keep a transaction history
- Save account data locally in JSON format

## Concepts Used

- Classes and objects
- Methods and constructors
- Dictionaries and lists
- Conditional statements and loops
- Exception handling
- JSON file handling
- Password hashing
- Date and time handling

## Project Structure

```text
mini-banking-system/
├── mini_banking_system.py
├── README.md
├── requirements.txt
└── .gitignore
```

The `bank_data.json` file is created locally when the program is used and is not meant to be committed because it contains account data.

## Running the project

No external packages are required.

```bash
python mini_banking_system.py
```

The program will open a simple menu where you can create an account, log in, perform transactions, view your balance, and check transaction history.

## Note

This is a learning project, not real banking software. The SHA-256 password hashing used here is not suitable for production authentication. Real financial systems need stronger password hashing, secure databases, authorization, encryption, rate limiting, and other security controls.

## Possible Improvements

- SQLite or PostgreSQL storage
- Account numbers
- Transfers between accounts
- PIN or OTP authentication
- Unit tests
- A graphical or web interface
- Better authentication and authorization

## Author

**Faqeeha Fathima**

B.Tech AI & Data Science
