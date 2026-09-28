# 🏦 Mini Banking System

> **Because apparently giving money to a Python program and trusting it with your balance is a perfectly reasonable learning exercise.**

A console-based **banking simulation built with Python and Object-Oriented Programming (OOP)**.

This project started as a simple Colab exercise using dictionaries, basic classes, login/signup logic, deposits, withdrawals, and balance checking. It has been restructured into a cleaner, reusable application with **OOP, validation, transaction history, password hashing, and local data persistence**.

> ⚠️ **Educational project — not actual banking software.**  
> Please do not deposit your life savings into a `.json` file. 😭

---

## ✨ What It Does

The application simulates a basic customer banking workflow:

**Create Account → Login → Manage Money → View Transactions → Logout**

### 🔐 Account & Authentication
- Create a new account
- Login using username and password
- Passwords are stored as SHA-256 hashes rather than plain text
- Prevent duplicate usernames
- Maintain an active logged-in user

### 💰 Banking Operations
- Deposit money
- Withdraw money
- Check current balance
- Block withdrawals when funds are insufficient
- Reject invalid or non-positive amounts

### 📜 Transaction Tracking
Every successful deposit or withdrawal records:
- Transaction type
- Amount
- Balance after transaction
- Date and time

### 💾 Data Persistence
Account information is saved locally in:

```text
bank_data.json
```

So the program does not completely forget everything the moment you close it. Character development. ✨

---

## 🧠 Technical Concepts Demonstrated

| Concept | Where It Is Used |
|---|---|
| Classes & Objects | `BankAccount`, `BankSystem` |
| Encapsulation | Banking operations inside account methods |
| Constructors | Initialising account state |
| Methods | Deposit, withdrawal, login, registration |
| Dictionaries | Storing account records |
| Lists | Transaction history |
| Conditional Logic | Validation and account operations |
| Loops | Interactive menus |
| Exception Handling | Safe numeric input and JSON loading |
| JSON | Local data persistence |
| File Handling | Reading/writing account data |
| Hashing | Password storage |
| `datetime` | Transaction timestamps |

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │    Mini Banking      │
                    │       System         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
       ┌──────▼──────┐                   ┌──────▼──────┐
       │  BankSystem  │                   │ BankAccount │
       └──────┬──────┘                   └──────┬──────┘
              │                                 │
       Authentication                    Banking Operations
       Registration                     ├── Deposit
       Persistence                      ├── Withdraw
       Current User                     ├── Balance
                                        └── Transactions
              │
              ▼
       ┌───────────────┐
       │ bank_data.json│
       └───────────────┘
```

---

## 🖥️ Example User Flow

```text
================================
       MINI BANKING SYSTEM
================================

1. Create Account
2. Login
3. Exit

Choose an option: 1

Create username: faqeeha
Create password: ********

Account created successfully.
```

After login:

```text
========== ACCOUNT MENU ==========

1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Transaction History
5. Logout

Choose an option: 1

Enter amount: ₹5000

₹5000.00 deposited successfully.
```

And if someone tries to withdraw more money than they have:

```text
Enter amount: ₹100000

Insufficient funds.
```

The bank has officially discovered the revolutionary concept of **not allowing negative balances**.

---

## 📁 Project Structure

```text
mini-banking-system/
│
├── mini_banking_system.py   # Main application
├── README.md                # Project documentation
├── requirements.txt         # Dependency information
└── .gitignore               # Prevents local/private files from being committed
```

`bank_data.json` is created automatically when the application runs and is intentionally excluded from Git.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd mini-banking-system
```

### 2. Run the application

```bash
python mini_banking_system.py
```

### 3. That's it.

No external packages are required because the project uses Python's standard library.

---

## 🔒 Security Note

This project intentionally includes **basic password hashing** so passwords are not stored directly as plain text.

However, this is **not production-grade authentication**.

Real financial applications require significantly stronger security practices, including:
- Password-specific hashing such as Argon2 or bcrypt
- Secure credential storage
- Encryption
- Authentication rate limiting
- Proper authorization
- Database security
- Audit logging
- Secure session management
- HTTPS and secure APIs

So yes — this project can simulate a bank.

**No, your bank should not be running this code.** 😭

---

## 📈 Future Improvements

- [ ] SQLite/PostgreSQL database
- [ ] Unique account numbers
- [ ] Money transfer between accounts
- [ ] PIN/OTP authentication
- [ ] Admin dashboard
- [ ] Automated unit tests with `pytest`
- [ ] REST API using Flask or FastAPI
- [ ] Streamlit interface
- [ ] Improved authentication and authorization
- [ ] Monthly transaction summaries
- [ ] Data analytics and spending visualisation

---

## 🎯 Why I Built This

This project was built to move beyond isolated Python exercises and practise how individual concepts work together inside a small application.

It combines:

**Python → OOP → Authentication → Validation → File Handling → JSON → State Management**

The goal is not to recreate a real bank.

The goal is to understand how a real application is **structured, validated, and maintained**.

---

## 👩‍💻 Author

**Faqeeha Fathima**

B.Tech AI & Data Science

> Building projects, breaking code, fixing it, and occasionally wondering why the code worked five minutes ago.

---

## ⭐ If You're Exploring the Project

Start with:

```text
mini_banking_system.py
```

Then look at:

1. `BankAccount` → how account operations are handled
2. `BankSystem` → authentication and persistence
3. `account_menu()` → user interaction
4. `main()` → application flow

That gives you the cleanest path through the code instead of diving into 200 lines and immediately questioning your life choices.
