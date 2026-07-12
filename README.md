
# 🏦 Bank Management System

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/JSON-Database-orange?style=for-the-badge&logo=json" alt="JSON">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

### A modern Bank Management System built with **Python** and **Streamlit**

*A simple, interactive banking application that allows users to create accounts, securely manage funds, update personal information, and perform banking operations through an intuitive web interface.*

</div>

---

# 📖 Overview

The **Bank Management System** is a beginner-friendly banking application developed using **Python** and **Streamlit**. It simulates core banking operations while demonstrating concepts such as data management, authentication, file handling, and CRUD operations.

Instead of using a traditional database, the application stores customer records in a **JSON file**, making it lightweight, portable, and easy to understand for students learning Python development.

This project focuses on writing clean, modular, and maintainable code while providing a responsive web interface.

---

# ✨ Features

## 👤 Account Management

* Create a new bank account
* Automatically generate a unique account number
* Secure account authentication using a 4-digit PIN
* Delete an existing account permanently

---

## 💰 Banking Operations

* Deposit money into an account
* Withdraw money securely
* Prevent withdrawals when the balance is insufficient
* Automatically update account balance

---

## 📄 Profile Management

* View account details
* Check current account balance
* Update customer name
* Update email address
* Change account PIN

---

## 🔒 Data Validation

* Unique account number generation
* PIN verification before sensitive operations
* Deposit and withdrawal validation
* Prevent invalid transactions
* Persistent local storage using JSON

---

# 🛠️ Tech Stack

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| **Python 3**  | Core programming language          |
| **Streamlit** | Interactive web interface          |
| **JSON**      | Local database for account storage |
| **random**    | Generate unique account numbers    |
| **string**    | Random account number creation     |
| **pathlib**   | File handling                      |
| **json**      | Read and write account information |

---

# 🏗️ Project Architecture

```text
                    User
                      │
                      ▼
             Streamlit Web Interface
                      │
                      ▼
        Bank Management Application
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
Create Account   Transactions   Account Settings
     │                │                │
     └────────────────┼────────────────┘
                      │
                      ▼
              data.json (Storage)
```

---

# 🚀 Getting Started

## Prerequisites

Make sure Python **3.8 or above** is installed.

Install Streamlit:

```bash
pip install streamlit
```

---

## Clone the Repository

```bash
git clone https://github.com/yourusername/bank-management-system.git

cd bank-management-system
```

---

## Run the Application

```bash
streamlit run app.py
```

After running the command, open your browser and visit:

```text
http://localhost:8501
```

---

# 📂 Project Structure

```text
bank-management-system/
│
├── app.py
├── data.json
├── README.md
│
├── assets/
│   └── screenshots/
│
└── requirements.txt
```

### Description

| File                 | Purpose                     |
| -------------------- | --------------------------- |
| **app.py**           | Main Streamlit application  |
| **data.json**        | Stores customer information |
| **README.md**        | Project documentation       |
| **requirements.txt** | Python dependencies         |

---

# 📌 Functional Modules

### 🆕 Create Account

* Register a new customer
* Generate a unique account number
* Set a secure 4-digit PIN

---

### 💵 Deposit

* Add money to an account
* Instantly update balance

---

### 💸 Withdraw

* Verify account PIN
* Validate available balance
* Prevent overdraft transactions

---

### 👤 View Account

* Display customer information
* Show available balance
* View account number

---

### ✏️ Update Profile

* Change customer name
* Update email address
* Change account PIN

---

### ❌ Delete Account

* Remove customer account
* Delete all stored account information

---

# 🔐 Security Features

* PIN-based authentication
* Account validation
* Unique account number generation
* Input validation
* Transaction verification
* Persistent local data storage

---

# 📈 Future Improvements

* Encrypt PINs using **bcrypt**
* Transaction history
* Mini statement generation
* Interest calculation
* Fund transfer between accounts
* Admin dashboard
* Login sessions
* SQLite integration
* PostgreSQL/MySQL support
* Account locking after multiple incorrect PIN attempts
* Email and SMS notifications
* Downloadable account statements (PDF)

---


# 🤝 Contributing

Contributions are welcome!

If you have ideas for improving the project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 👨‍💻 Author

Developed as a Python project to demonstrate:

* Object-Oriented Programming
* CRUD Operations
* File Handling
* JSON Data Storage
* Streamlit Web Development
* Basic Banking System Design

---

# 📄 License

This project is licensed under the **MIT License**.

---



</div>
