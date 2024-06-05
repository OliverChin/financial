# Financial Tracker

## Overview

This is a simple command-line-based financial tracker that allows users to register, login(with username or email address), and manage their accounts. Users can add income, record expenses, and view summaries and transactions. The system also supports account deletion and password changes.

## Features

- **Login with Username or Email**: Users can login using either their username or email address.
- **Register New Account**: New users can register with a unique username and valid email address.
- **Password Validation**: Ensures that passwords meet the specified requirements.
- **Email Validation**: Ensures that email addresses are valid and not already in use.
- **Dashboard**: Users are directed to a dashboard after logging in, where they can manage their finances.
- **Add Income and Expenses**: Users can add income and record expenses, which are stored in text files.
- **View Summary**: Users can view a summary of their total income, expenses, and remaining balance.
- **View Transaction History**: Users can view their transaction history and the dates of those transactions.
- **Change Password**: Users can change their password after verifying their current password.
- **Delete Account**: Users can delete their account, which will remove all their data from the system.

## File Structure

- `accounts.txt`: Stores username and password pairs.
- `email_password.txt`: Stores email and password pairs.
- `email_to_username.txt`: Maps email addresses to usernames.
- `username_to_email.txt`: Maps usernames to email addresses.
- `incomes_<username>.txt`: Stores income records for a user.
- `expenses_<username>.txt`: Stores expense records for a user.
- `transactions_<username>.txt`: Stores transaction history for a user.

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/OliverChin/financial.git
    cd financial
    ```

2. **Create Required Files**

    Ensure that the following files exist in the same directory as the script:
    
    - `accounts.txt`
    - `email_password.txt`
    - `email_to_username.txt`
    - `username_to_email.txt`

    These files should be empty initially or contain valid data if you are continuing from previous sessions.

3. **Run the Script**

    Execute the script using Python:

    ```bash
    python project.py
    ```

## Usage

### Main Menu

- **1. Login to an existing account**: Login with your username or email.
- **2. Register a new account**: Register a new account by providing a unique username, valid email, and a secure password.

### Dashboard Menu

- **1. Add Income**: Add an income entry.
- **2. Add Expense**: Add an expense entry.
- **3. View Summary**: View a summary of your financials.
- **4. View Transaction History**: View the history of your transactions.
- **5. Change Password**: Change your account password.
- **6. Delete Account**: Delete your account.
- **7. Logout**: Logout from the account.

## Functions

### Main Functions

- `main()`: Displays the main menu and directs users to login or register.
- `login()`: Manages the login process, allowing login with either username or email.
- `register()`: Handles user registration, including username and email validation, and password creation.

### Supporting Functions

- `login_username()`: Handles login using a username.
- `login_email()`: Handles login using an email address.
- `dashboard(username)`: Displays the user dashboard.
- `income(username, date)`: Allows users to add income.
- `expenses(username, date)`: Allows users to add expenses.
- `summary(username)`: Displays a summary of incomes and expenses.
- `transactions(username)`: Displays the transaction history.
- `change_password(username)`: Allows users to change their password.
- `self_destruct(username)`: Deletes the user's account and associated data.

### Utility Functions

- `check_password(password)`: Validates the password.
- `check_email(email, email_password)`: Validates the email address.
- `confirm_password(password, username, accounts)`: Confirms the password.
- `load()`: Loads data from the system into the text files.

## Notes

- This system uses text files for data storage. Ensure that the files are properly maintained and backed up.
- The email and password validation uses regular expressions to ensure proper formatting.
- Passwords are stored in plain text for simplicity. For a production system, consider using a secure hashing algorithm for storing passwords.


