import time
import json
from datetime import datetime

# Separate lists for personal and work accounts
accounts = {
    "Personal": {"income_list": [], "expense_list": []},
    "Work": {"income_list": [], "expense_list": []}
}

# Function to display text letter by letter
def display_text(text, Time=0.03):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(Time)
    print()

# Function to validate date format
def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Function to choose user account
def choose_account():
    personal_password = "personal123"
    work_password = "work123"
    
    while True:
        display_text("\nChoose an account:\n1. Personal Account\n2. Work Account\n")
        choice = int(input(" Enter the number of your choice: "))
        if choice == 1:
            while True:
                password = input("\nEnter password for Personal Account: ")
                if password == personal_password:
                    display_text("\nPersonal Account selected.\n")
                    return "Personal"
                else:
                    display_text("\nIncorrect password. Please try again.\n")
        elif choice == 2:
            while True:
                password = input("\nEnter password for Work Account: ")
                if password == work_password:
                    display_text("\nWork Account selected.\n")
                    return "Work"
                else:
                    display_text("\nIncorrect password. Please try again.\n")
        else:
            display_text("\nInvalid choice. Please try again.\n")

# Function to add income
def add_income(account):
    display_text("\nEnter details for the new income:\n")
    description = input("Enter Description: ")
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount < 0:
                display_text("\nInvalid input. Please enter a positive number.\n")
                continue
            break
        except ValueError:
            display_text("\nInvalid input. Please enter a valid number.\n")
    while True:
        date = input("Enter Date (Day-Month-Year): ")
        if validate_date(date):
            break
        else:
            display_text("\nInvalid date. Please enter in DD-MM-YYYY format.\n")
    accounts[account]["income_list"].append({"description": description, "amount": amount, "date": date})
    display_text(f"Income added to {account} account: {description} --> {amount} pounds on {date}\n")
    
    # Calculate the total income
    total_income = 0
    for item in accounts[account]["income_list"]:
        total_income += item['amount']
    
    # Calculate the total expenses
    total_expenses = 0
    for item in accounts[account]["expense_list"]:
        total_expenses += item['amount']
    
    # Calculate the remaining balance
    remaining_balance = total_income - total_expenses
    
    # Display the remaining balance
    display_text(f"Your balance is now ---> {remaining_balance} pounds\n")

# Function to add expense
def add_expense(account):
    display_text("\nEnter details for the new expense:\n")
    category = input("Enter Category (ex: Food, Transport): ")
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount < 0:
                display_text("\nInvalid input. Please enter a positive number.\n")
                continue
            break
        except ValueError:
            display_text("\nInvalid input. Please enter a valid number.\n")
    
    # Calculate the current remaining balance using for loops
    total_income = 0
    for item in accounts[account]["income_list"]:
        total_income += item['amount']

    total_expenses = 0
    for item in accounts[account]["expense_list"]:
        total_expenses += item['amount']

    remaining_balance = total_income - total_expenses
    
    # Check if there is enough balance to cover the expense
    if amount > remaining_balance:
        display_text("You do not have enough income to cover this expense. Please add more income.\n")
        display_text(f"Your balance is ---> {remaining_balance} pounds\n")
        return
    
    while True:
        date = input("Enter Date (Day-Month-Year): ")
        if validate_date(date):
            break
        else:
            display_text("\nInvalid date. Please enter in DD-MM-YYYY format.\n")
    
    accounts[account]["expense_list"].append({"category": category, "amount": amount, "date": date})
    display_text(f"Expense added to {account} account: {category} --> {amount} pounds on {date}\n")
    
    # display the remaining balance
    remaining_balance -= amount
    display_text(f"Remaining Balance: {remaining_balance} pounds\n")

# Function to display all income
def view_incomes(account):
    display_text(f"\nYour Income Records for {account} account:\n")
    if not accounts[account]["income_list"]:
        display_text("No income records available.\n")
    else:
        for income in accounts[account]["income_list"]:
            display_text(f"Description: {income['description']}, Amount: {income['amount']}, Date: {income['date']}\n")

# Function to display all expenses
def view_expenses(account):
    display_text(f"\nYour Expense Records for {account} account:\n")
    if not accounts[account]["expense_list"]:
        display_text("No expense records available.\n")
    else:
        for expense in accounts[account]["expense_list"]:
            display_text(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}\n")

# Function to delete an entry
def delete_entry(account):
    display_text("\nChoose what to delete:\n1. Income\n2. Expense\n")
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        entry_list = accounts[account]["income_list"]
        entry_type = "income"
    elif choice == "2":
        entry_list = accounts[account]["expense_list"]
        entry_type = "expense"
    else:
        display_text("\nInvalid choice.\n")
        return
    
    if not entry_list:
        display_text(f"\nNo {entry_type} records to delete.\n")
        return
    
    counter = 1
    for entry in entry_list:
        if entry_type == "income":
            display_text(f"{counter}. Description: {entry['description']}, Amount: {entry['amount']}, Date: {entry['date']}\n")
        else:
            display_text(f"{counter}. Category: {entry['category']}, Amount: {entry['amount']}, Date: {entry['date']}\n")
        counter += 1
    
    try:
        index = int(input(f"Enter the number of the {entry_type} to delete: ")) - 1
        if 0 <= index < len(entry_list):
            removed = entry_list.pop(index)
            display_text(f"Deleted {entry_type}: {removed}\n")
        else:
            display_text("\nInvalid choice.\n")
            return
    except ValueError:
        display_text("\nInvalid input. Please enter a number.\n")

# Function to edit income or expense
def edit_entry(account):
    display_text("\nChoose what to edit:\n1. Income\n2. Expense\n")
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        entry_list = accounts[account]["income_list"]
        entry_type = "income"
    elif choice == "2":
        entry_list = accounts[account]["expense_list"]
        entry_type = "expense"
    else:
        display_text("\nInvalid choice.\n")
        return
    
    if not entry_list:
        display_text(f"\nNo {entry_type} records to edit.\n")
        return
    
    for i, entry in enumerate(entry_list, 1):
        display_text(f"{i}. {entry}\n")
    
    try:
        index = int(input(f"Enter the number of the {entry_type} to edit: ")) - 1
        if 0 <= index < len(entry_list):
            entry = entry_list[index]
            for key in entry:
                while True:
                    new_value = input(f"Enter new {key} (current: {entry[key]}): ").strip()
                    if new_value:
                        if key == "amount":
                            try:
                                new_amount = float(new_value)
                                if new_amount < 0:
                                    display_text("\nInvalid input. Please enter a positive number.\n")
                                    continue
                                entry[key] = new_amount
                                break
                            except ValueError:
                                display_text("\nInvalid input. Please enter a valid number.\n")
                                continue
                        elif key == "date":
                            if validate_date(new_value):
                                entry[key] = new_value
                                break
                            else:
                                display_text("\nInvalid date. Please enter in DD-MM-YYYY format.\n")
                                continue
                        else:
                            entry[key] = new_value
                            break
                    else:
                        break
            display_text(f"Updated {entry_type}: {entry}\n")
        else:
            display_text("\nInvalid choice.\n")
            return
    except ValueError:
        display_text("\nInvalid input. Please enter a number.\n")

# Function to show total summary
def show_summary(account):
    total_income = 0
    for item in accounts[account]["income_list"]:
        total_income += item['amount']  # Add each income amount to the total

    total_expenses = 0
    for item in accounts[account]["expense_list"]:
        total_expenses += item['amount']  # Add each expense amount to the total

    remaining_balance = total_income - total_expenses  # Calculate the balance

    print(f"Total Income: {total_income} pounds")
    print(f"Total Expenses: {total_expenses} pounds")
    print(f"Remaining Balance: {remaining_balance} pounds")

# Function to save data to a JSON file
def save_to_file():
    with open("budget_data.json", "w") as file:
        json.dump(accounts, file, indent=4)
    display_text("Data saved successfully to budget_data.json!\n")

# Function to load data from a JSON file
def load_from_file():
    global accounts
    try:
        with open("budget_data.json", "r") as file:
            data = json.load(file)
            accounts = data
            display_text("Data loaded successfully from budget_data.json!\n")
    except FileNotFoundError:
        display_text("No saved data found. Starting with empty records.\n")

# Main menu
def main_menu():
    load_from_file()
    account = choose_account()
    while True:
        display_text(f"\n--- {account} Budget Tracker ---\n")
        display_text("1. Add Income\n")
        display_text("2. Add Expense\n")
        display_text("3. View Incomes\n")
        display_text("4. View Expenses\n")
        display_text("5. Show Monthly Summary\n")
        display_text("6. Delete Entry\n")
        display_text("7. Edit Entry\n")
        display_text("8. Switch Account\n")
        display_text("9. Save and Exit\n")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_income(account)
        elif choice == "2":
            if not accounts[account]["income_list"]:
                display_text("\nPlease enter income first.\n")
            else:
                add_expense(account)
        elif choice == "3":
            view_incomes(account)
        elif choice == "4":
            view_expenses(account)
        elif choice == "5":
            show_summary(account)
        elif choice == "6":
            delete_entry(account)
        elif choice == "7":
            edit_entry(account)
        elif choice == "8":
            account = choose_account()
        elif choice == "9":
            save_to_file()
            display_text("Thank you for using the Budget Tracker. Goodbye!\n")
            break
        else:
            display_text("Invalid choice. Please try again.\n")

# Starting the program
display_text("Welcome to the Personal Budget Tracker!\nThis program helps you track your income and expenses.\n", 0.08)
main_menu()