# 🏦 Bank Management System 
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B) 
![License](https://img.shields.io/badge/License-MIT-green) 

A lightweight, interactive Bank Management System built with Python and Streamlit. This application provides a clean web interface for users to create accounts, manage their finances, and securely update their details using file-based JSON storage.
---

## ✨ Features * **Create Account:** Register a new bank account with secure 4-digit PIN authentication. Automatically generates a unique, randomized Account Number. * **Deposit & Withdraw:** Securely add or remove funds from your account with real-time balance updates. Includes limits and insufficient funds validation. * **Account Details:** View your current profile information and account balance at any time. * **Update Profile:** Modify your name, email, or PIN seamlessly while keeping core data (Account Number, Balance, Age) immutable. * **Delete Account:** Permanently remove your account and data from the system. * **Secure Storage:** All user data is securely stored and retrieved using a local data.json file.

<h2>🛠️ Tech Stack</h2>

<table>
<tr>
<th>Technology</th>
<th>Description</th>
</tr>

<tr>
<td><strong>Language</strong></td>
<td>Python 3</td>
</tr>

<tr>
<td><strong>Framework</strong></td>
<td>Streamlit</td>
</tr>

<tr>
<td><strong>Database</strong></td>
<td>JSON File Storage</td>
</tr>

<tr>
<td><strong>Libraries</strong></td>
<td>json, random, string, pathlib</td>
</tr>

</table>

---

<h2>🚀 Getting Started</h2>

<h3>Prerequisites</h3>

<ul>
<li>Python 3.8 or above</li>
<li>Streamlit</li>
</ul>

Install Streamlit:

```bash
pip install streamlit
```

---

<h2>📥 Installation</h2>

Clone the repository:

```bash
git clone https://github.com/yourusername/bank-management-system.git
cd bank-management-system
```

Run the application:

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

---

<h2>📂 Project Structure</h2>

```text
bank-management-system/
│
├── app.py             # Main Streamlit application
├── data.json          # JSON database (auto-generated)
├── README.md          # Documentation
└── requirements.txt   # Project dependencies (optional)
```

---

<h2>⚙️ Functionalities</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Create Account</td>
<td>Create a new user account with a unique account number.</td>
</tr>

<tr>
<td>Deposit Money</td>
<td>Add money to the account securely.</td>
</tr>

<tr>
<td>Withdraw Money</td>
<td>Withdraw money after validating the available balance.</td>
</tr>

<tr>
<td>View Details</td>
<td>Display account information and current balance.</td>
</tr>

<tr>
<td>Update Details</td>
<td>Modify user name, email, or PIN.</td>
</tr>

<tr>
<td>Delete Account</td>
<td>Permanently remove an account from the system.</td>
</tr>

</table>

---

<h2>🔮 Future Enhancements</h2>

<ul>
<li>🔐 Encrypt PINs using <strong>bcrypt</strong>.</li>

<li>📜 Add transaction history.</li>

<li>🗄️ Replace JSON storage with SQLite or PostgreSQL.</li>

<li>👥 Multi-user session support.</li>

<li>📊 Dashboard with transaction analytics.</li>

<li>📧 Email notifications for deposits and withdrawals.</li>

</ul>

---

<h2>🤝 Contributing</h2>

Contributions, issues, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

<h2>📝 License</h2>

This project is licensed under the <strong>MIT License</strong>.

---

<div align="center">

### ⭐ If you found this project useful, don't forget to star the repository!

Made with ❤️ using Python & Streamlit

</div>
