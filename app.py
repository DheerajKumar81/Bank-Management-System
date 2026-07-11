import streamlit as st
import json
import random
import string
from pathlib import Path

# --- Configuration & Setup ---
st.set_page_config(page_title="Bank Management System", page_icon="🏦")

# Make sure the data directory and file exist
DATA_FILE = 'data.json'
if not Path(DATA_FILE).exists():
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# --- Helper Functions ---
def load_data():
    try:
        with open(DATA_FILE, 'r') as fs:
            return json.load(fs)
    except Exception as err:
        st.error(f"Error reading database: {err}")
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as fs:
        json.dump(data, fs, indent=4)

def generate_account_no():
    alpha = random.choices(string.ascii_letters, k=3)
    num = random.choices(string.digits, k=3)
    splchars = random.choices("!@#$%^&*", k=1)
    acc_id = alpha + num + splchars
    random.shuffle(acc_id)
    return "".join(acc_id)

def get_user(data, acc_no, pin):
    for user in data:
        if user['AccountNo.'] == acc_no and user['pin'] == pin:
            return user
    return None

# --- Main App ---
st.title("🏦 Bank Management System")

# Sidebar Menu
menu = [
    "Create Account", 
    "Deposit Money", 
    "Withdraw Money", 
    "Show Details", 
    "Update Details", 
    "Delete Account"
]
choice = st.sidebar.selectbox("Select Action", menu)

data = load_data()

# 1. Create Account
if choice == "Create Account":
    st.subheader("Create a New Account")
    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        email = st.text_input("Email Address")
        pin = st.text_input("Create 4-Digit PIN", type="password", max_chars=4)
        
        submit = st.form_submit_button("Create Account")
        
        if submit:
            if age < 18:
                st.error("Sorry, you must be at least 18 years old to create an account.")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("Please enter a valid 4-digit PIN.")
            elif not name or not email:
                st.error("Please fill out all fields.")
            else:
                new_account_no = generate_account_no()
                info = {
                    "name": name,
                    "age": age,
                    "email": email,
                    "pin": int(pin),
                    "AccountNo.": new_account_no,
                    "Balance": 0
                }
                data.append(info)
                save_data(data)
                
                st.success("Account created successfully!")
                st.info(f"**Please note down your Account Number:** `{new_account_no}`")
                st.json(info)

# 2. Deposit Money
elif choice == "Deposit Money":
    st.subheader("Deposit Money")
    with st.form("deposit_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("4-Digit PIN", type="password")
        amount = st.number_input("Amount to Deposit", min_value=0, step=100)
        
        submit = st.form_submit_button("Deposit")
        
        if submit:
            if pin.isdigit():
                user = get_user(data, acc_no, int(pin))
                if not user:
                    st.error("Sorry, Invalid Account Number or PIN.")
                else:
                    if amount > 10000 or amount <= 0:
                        st.error("Amount must be between 1 and 10,000.")
                    else:
                        user['Balance'] += amount
                        save_data(data)
                        st.success(f"Successfully deposited ₹{amount}. New Balance: ₹{user['Balance']}")
            else:
                st.error("Invalid PIN format.")

# 3. Withdraw Money
elif choice == "Withdraw Money":
    st.subheader("Withdraw Money")
    with st.form("withdraw_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("4-Digit PIN", type="password")
        amount = st.number_input("Amount to Withdraw", min_value=0, step=100)
        
        submit = st.form_submit_button("Withdraw")
        
        if submit:
            if pin.isdigit():
                user = get_user(data, acc_no, int(pin))
                if not user:
                    st.error("Sorry, Invalid Account Number or PIN.")
                else:
                    if user['Balance'] < amount:
                        st.error(f"Insufficient funds! Your current balance is ₹{user['Balance']}.")
                    elif amount <= 0:
                        st.error("Please enter a valid amount to withdraw.")
                    else:
                        user['Balance'] -= amount
                        save_data(data)
                        st.success(f"Successfully withdrew ₹{amount}. New Balance: ₹{user['Balance']}")
            else:
                st.error("Invalid PIN format.")

# 4. Show Details
elif choice == "Show Details":
    st.subheader("Account Details")
    with st.form("details_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("4-Digit PIN", type="password")
        
        submit = st.form_submit_button("Fetch Details")
        
        if submit:
            if pin.isdigit():
                user = get_user(data, acc_no, int(pin))
                if not user:
                    st.error("Sorry, Invalid Account Number or PIN.")
                else:
                    st.success("Data Found!")
                    st.json(user)
            else:
                st.error("Invalid PIN format.")

# 5. Update Details
elif choice == "Update Details":
    st.subheader("Update Account Details")
    st.info("Note: You cannot change your Age, Account Number, or Balance.")
    
    with st.form("update_form"):
        st.write("**Step 1: Authenticate**")
        acc_no = st.text_input("Account Number")
        pin = st.text_input("Current 4-Digit PIN", type="password")
        
        st.write("**Step 2: Enter New Details (Leave blank if no change)**")
        new_name = st.text_input("New Name")
        new_email = st.text_input("New Email")
        new_pin = st.text_input("New 4-Digit PIN (Optional)", type="password", max_chars=4)
        
        submit = st.form_submit_button("Update Details")
        
        if submit:
            if pin.isdigit():
                user = get_user(data, acc_no, int(pin))
                if not user:
                    st.error("Sorry, Invalid Account Number or PIN.")
                else:
                    updated = False
                    if new_name.strip():
                        user['name'] = new_name.strip()
                        updated = True
                    if new_email.strip():
                        user['email'] = new_email.strip()
                        updated = True
                    if new_pin.strip() and len(new_pin) == 4 and new_pin.isdigit():
                        user['pin'] = int(new_pin)
                        updated = True
                        
                    if updated:
                        save_data(data)
                        st.success("Details updated successfully!")
                        st.json(user)
                    else:
                        st.warning("No changes were made.")
            else:
                st.error("Invalid current PIN format.")

# 6. Delete Account
elif choice == "Delete Account":
    st.subheader("Delete Account")
    st.warning("Warning: This action is permanent and cannot be undone!")
    
    with st.form("delete_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("4-Digit PIN", type="password")
        confirm = st.checkbox("I understand that my account will be permanently deleted.")
        
        submit = st.form_submit_button("Delete My Account")
        
        if submit:
            if not confirm:
                st.error("You must check the confirmation box to proceed.")
            elif pin.isdigit():
                user = get_user(data, acc_no, int(pin))
                if not user:
                    st.error("Sorry, Invalid Account Number or PIN.")
                else:
                    data.remove(user)
                    save_data(data)
                    st.success("Account deleted successfully!")
            else:
                st.error("Invalid PIN format.")