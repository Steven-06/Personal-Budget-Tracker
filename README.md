# Personal Budget Tracker

A Python-based Personal Budget Tracker designed to help users manage and monitor their income and expenses through a simple command-line interface.

The application supports separate **Personal** and **Work** accounts with password-protected access. Users can add income and expenses with descriptions or categories, amounts, and dates, while the program automatically calculates the total income, total expenses, and remaining balance.

Users can also view, edit, and delete financial records. The application validates entered amounts and dates and checks whether the user has enough balance before allowing an expense to be added.

Financial data can be saved to and loaded from a **JSON file**, allowing users to keep their records between program sessions.

## Features

* Add and manage income records
* Add categorized expense records
* Separate Personal and Work accounts
* Password-protected account access
* View income and expense records
* Edit and delete financial entries
* Calculate total income, expenses, and remaining balance
* Check available balance before adding expenses
* Validate amounts and dates
* Save and load data using JSON
* Switch between accounts

## Technologies

* Python
* JSON
* `datetime`
* Command-Line Interface (CLI)

## How to Run

```bash
Persnoal_Budget_Tracker.py
```

The application will guide you through account selection and provide a menu for managing your financial records.
