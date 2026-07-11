# 🏦 Bank Management System

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight, interactive Bank Management System built with Python and Streamlit. This application provides a clean web interface for users to create accounts, manage their finances, and securely update their details using file-based JSON storage.

## ✨ Features

*   **Create Account:** Register a new bank account with secure 4-digit PIN authentication. Automatically generates a unique, randomized Account Number.
*   **Deposit & Withdraw:** Securely add or remove funds from your account with real-time balance updates. Includes limits and insufficient funds validation.
*   **Account Details:** View your current profile information and account balance at any time.
*   **Update Profile:** Modify your name, email, or PIN seamlessly while keeping core data (Account Number, Balance, Age) immutable.
*   **Delete Account:** Permanently remove your account and data from the system.
*   **Secure Storage:** All user data is securely stored and retrieved using a local `data.json` file.

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Frontend / Framework:** Streamlit
*   **Database:** Local JSON File Storage (`json` module)
*   **Libraries:** `random`, `string`, `pathlib`

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed on your system. You will also need to install the Streamlit library.

```bash
pip install streamlit

🏦 Bank Management System
A lightweight, interactive Bank Management System built with Python and Streamlit. This application provides a clean web interface for users to create accounts, manage their finances, and securely update their details using file-based JSON storage.

✨ Features
Create Account: Register a new bank account with secure 4-digit PIN authentication. Automatically generates a unique, randomized Account Number.

Deposit & Withdraw: Securely add or remove funds from your account with real-time balance updates. Includes limits and insufficient funds validation.

Account Details: View your current profile information and account balance at any time.

Update Profile: Modify your name, email, or PIN seamlessly while keeping core data (Account Number, Balance, Age) immutable.

Delete Account: Permanently remove your account and data from the system.

Secure Storage: All user data is securely stored and retrieved using a local data.json file.

🛠️ Tech Stack
Language: Python 3

Frontend / Framework: Streamlit

Database: Local JSON File Storage (json module)

Libraries: random, string, pathlib

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Make sure you have Python installed on your system. You will also need to install the Streamlit library.

Bash
pip install streamlit
Installation & Execution
Clone the repository:

Bash
git clone https://github.com/yourusername/bank-management-system.git
cd bank-management-system
Run the application:

Bash
streamlit run app.py
Open your browser:
The application will automatically launch in your default web browser at http://localhost:8501.

📁 Project Structure
Plaintext
bank-management-system/
│
├── app.py             # Main Streamlit application script
├── data.json          # Database file (auto-generated upon first run)
└── README.md          # Project documentation
🔮 Future Enhancements
Implement password hashing (e.g., bcrypt) for PINs to enhance security.

Add a transaction history log to track previous deposits and withdrawals.

Migrate from JSON file storage to an SQLite or PostgreSQL database for better scalability.

Implement multi-user session states so multiple users can interact simultaneously without data conflicts.

🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page if you want to contribute.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
