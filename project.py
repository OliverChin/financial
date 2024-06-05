import re
from datetime import date
import os

accounts = {}
email_password = {}
email_to_username = {}
username_to_email = {}

#Loading data from text files
print("Loading....")
with open('accounts.txt', 'r') as f:
    users = f.readlines()
for user in users:
    username, password = user.strip().split(",")
    accounts[username] = password

with open('email_password.txt') as f:
    users = f.readlines()
for user in users:
    email, password = user.strip().split(",")
    email_password[email] = password


with open('email_to_username.txt', 'r') as f:
    users = f.readlines()
for user in users:
    email, username = user.strip().split(",")
    email_to_username[email] = username

with open('username_to_email.txt', 'r') as f:
    users = f.readlines()
for user in users:
    username, email = user.strip().split(",")
    username_to_email[username] = email

    

def main():
    print("---------------------------------")
    print("Menu")
    print("---------------------------------")
    print("1. Login to an existing account")
    print("2. Register a new account")
    print("---------------------------------")
    choice = 0
    while choice != 1 and choice != 2:
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid choice")
    if choice == 1:
        username = login()
        print("Login Successful!")
    if choice == 2:
        username = register()
        print("Registration Successful!")
    #After user is logged in they are sent to the dashboard
    dashboard(username)
    

    



#Function that deals with logins
def login():
    print("---------------------------------")
    print("Login")
    print("---------------------------------")
    print("1. Login with username")
    print("2. Login with email address")
    print("---------------------------------")
    choice = 0
    while choice != 1 and choice != 2:
        try:
            choice = int(input("Enter the number of your choice: "))
            print("---------------------------------")
        except ValueError:
            print("---------------------------------")
            print("Invalid choice")

    username = ""

    if choice == 1:
        username = login_username()

    elif choice == 2:
        username = email_to_username[login_email()]

    return username
        
    

#Function that deals with logins using usernames
def login_username():
    username = input("Username: ")
    password = input("Password: ")
    username = username.strip()
    password = password.strip()
   
    while username not in accounts or accounts[username] != password:
        print("---------------------------------")
        print("Wrong username or password")
        username = input("Re-enter username: ")
        password = input("Re-enter password: ")
    print("Login successful")

    return username

#Function that deals with logins using email addresses
def login_email():
    #Prompts user for email address
    email = input("Email address: ")
    password = input("Password: ")
    email = email.strip()
    password = password.strip()
    #Repromts user if email address or password is invalid
    while email not in email_password or email_password[email] != password:
        print("Wrong email address or password")
        email = input("Re-enter email address: ")
        password = input("Re-enter password: ")
    print("Login successful!")

    return email

#Function that deals with registration of new users
def register():
    print("---------------------------------")
    print("Register")
    print("---------------------------------")
    #Prompts user for username
    username = input("Enter username: ")
    while username in accounts:
        print("That username is already taken. Please choose a different username.")
        username = input("Re-enter username: ")

    #Prompts user for email address
    email = input("Enter email address: ")
    email = check_email(email, email_password)

    #Prompts user for password
    print("---------------------------------")
    print("Password must:")
    print("-Contain 8 to 16 characters")
    print("-Contain at least 1 number")
    print("-Not contain any spaces")
    print("---------------------------------")
    password = input("Enter password: ")
    password = check_password(password)
    
    #Creates new files for the user
    open(f'incomes_{username}.txt', 'w').close()
    open(f'expenses_{username}.txt', 'w').close()
    open(f'transactions_{username}.txt', 'w').close()

    #Updates records
    accounts[username] = password
    email_password[email] = password
    email_to_username[email] = username
    username_to_email[username] = email
    load()

    return username

def dashboard(username):
    while True:
        #Today's date
        day = str(date.today())
        print("---------------------------------")
        print(f"Dashboard - logged in as {username}")
        print("---------------------------------")
        print("What would you like to do?")
        print("---------------------------------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Transaction History")
        print("5. Change Password")
        print("6. Delete Account")
        print("7. Logout")
        print("---------------------------------")
        choice = 0
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7:
            try:
                choice = int(input("Enter the number of your choice: "))
            except ValueError:
                print("Invalid choice")
        print("---------------------------------")
        if choice == 1:
            income(username, day)

        elif choice == 2:
            expenses(username, day)
        
        elif choice == 3:
            summary(username)
        
        elif choice == 4:
            transactions(username)

        elif choice == 5:
            change_password(username)

        elif choice == 6:
            self_destruct(username)
            
        else:
            exit("Successfully Logged out")
            

        

def income(username, date):
    print("Add Income")
    print("---------------------------------")
    income = input("Enter income: ")
    while not income.isdigit():
        print("Invalid Income")
        income = input("Re-enter income: ")
    income = int(income)

    with open(f'incomes_{username}.txt', 'a') as f:
        f.write(f"{income}\n")
    with open(f'transactions_{username}.txt', 'a') as f:
        f.write(f"{income},{date}\n")
    print("---------------------------------")
    print("Income Successfully Added!")
    print("---------------------------------")
    choice = input("Press any key to return to dashboard: ")
    dashboard(username)
    
def expenses(username, date):
    print("Add Expense")
    print("---------------------------------")
    expense = input("Enter expense: ")
    print("---------------------------------")
    while not expense.isdigit():
        print("Invalid Expense")
        expense = input("Re-enter expense: ")
    expense = int(expense)

    with open(f'expenses_{username}.txt', 'a') as f:
        f.write(f"{expense}\n")
    with open(f'transactions_{username}.txt', 'a') as f:
        f.write(f"-{expense},{date}\n")
    print("Expense Successfully Added!")
    print("---------------------------------")
    choice = input("Press any key to return to dashboard: ")
    dashboard(username)

def summary(username):
    with open(f'incomes_{username}.txt', 'r') as f:
        users = f.readlines()
    total_income = 0
    for income in users:
        total_income += int(income.strip())
    
    with open(f'expenses_{username}.txt', 'r') as f:
        users = f.readlines()
    total_expenses = 0
    for expense in users:
        total_expenses += int(expense.strip())
    print("Summary")
    print("---------------------------------")
    print(f"Total Incomes    : {total_income}")
    print(f"Total Expenses   : {total_expenses}")
    print(f"Remainder balance: {total_income - total_expenses}")
    print("---------------------------------")
    choice = input("Press any key to return to dashboard: ")
    dashboard(username)

def transactions(username):
    with open(f'transactions_{username}.txt', 'r') as f:
        transactions = f.readlines()
    print("Date        |  Amount")
    print("---------------------------------")
    for transaction in transactions:
        value, date= transaction.strip().split(",")
        print(f"{date}  |  {value}")
    
    print("---------------------------------")
    choice = input("Press any key to return to dashboard: ")
    dashboard(username)

def change_password(username):
    print("Change Password")
    print("---------------------------------")
    old_password = input("Enter your old password: ")
    confirm_password(old_password, username, accounts)
    print("---------------------------------")
    print("Password must:")
    print("-Contain 8 to 16 characters")
    print("-Contain at least 1 number")
    print("-Not contain any spaces")
    print("---------------------------------")
    new_password = input("Enter your new password: ")
    new_password = check_password(new_password)
    new_password1 = input("Re-enter your new password: ")
    while new_password != new_password1:
        print("---------------------------------")
        print("Passwords do not match")
        new_password = input("Enter your new password: ")
        new_password = check_password(new_password)
        new_password1 = input("Re-enter your new password: ")
    #Changing password in records
    accounts[username] = new_password
    email = username_to_email[username]
    email_password[email] = new_password
    load()
    print("---------------------------------")
    print("Password has been successfully changed!")
    print("---------------------------------")
    choice = input("Press any key to return to dashboard: ")
    dashboard(username)

def self_destruct(username):
    print("Delete Account")
    print("---------------------------------")
    password = input("Enter password: ")
    confirm_password(password, username, accounts)
    confirm = input("Are you sure? y/n: ")
    if confirm == "n":
        dashboard(username)
    elif confirm == "y":
        pass
    else:
        print("Invalid choice")
        dashboard(username)

    email = username_to_email[username]

    del accounts[username]
    del email_password[email]
    del email_to_username[email]
    del username_to_email[username]

    os.remove(f"incomes_{username}.txt")
    os.remove(f"expenses_{username}.txt")
    os.remove(f"transactions_{username}.txt")
    load()
    print("Account Successfully Deleted!")
    exit()

#Load function uploads all the current accounts' information
def load():
    with open('accounts.txt', 'w') as f:
        for username in accounts:
            f.write(f"{username},{accounts[username]}\n")
    
    with open('email_password.txt', 'w') as f:
        for email in email_password:
            f.write(f"{email},{email_password[email]}\n")

    with open('email_to_username.txt', 'w') as f:
        for email in email_to_username:
            f.write(f"{email},{email_to_username[email]}\n")

    with open('username_to_email.txt', 'w') as f:
        for username in username_to_email:
            f.write(f"{username},{username_to_email[username]}\n")

#Checks for a valid password
def check_password(password):
    count_digits = 0

    #Counts the number of digits in the password
    for letter in password:
        if letter.isdigit():
            count_digits += 1
    #Validates the requirements for the password
    while len(password) < 8 or len(password) > 16 or " " in password or count_digits < 1:
        print("Password does not follow requirements")
        print("Password must:")
        print("-Contain 8 to 16 characters")
        print("-Contain at least 1 number")
        print("-Not contain any spaces")
        password = input("Re-enter password: ")
        count_digits = 0 
        for letter in password:
            if letter.isdigit():
                count_digits += 1
    return password

#Checks for a valid email address
def check_email(email, email_password):
    while email in email_password:
        print("An account already exists with that email address")
        email = input("Re-enter email address: ")

    valid_email = False

    #Uses regular expression to check validity of email address
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        valid_email = True

    #Loops until a valid email address is entered
    while not valid_email:
        print("Email is invalid")
        email = input("Re-enter email address: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            valid_email = True

    return email

#Ensures password entered matches the account's password
def confirm_password(password, username, accounts):
    while password != accounts[username]:
        print("Incorrect Password")
        password = input("Re-enter password: ")

    return True
        

if __name__ == "__main__":
    main()
