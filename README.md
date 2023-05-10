# Project Name: Group Payment Tracker

## Description
This is a Django project that allows a group of people to keep track of their payments and expenses during a trip, event or any other group activity. The application allows members to create an account, add their expenses, and keep track of the balance between the members. The system can calculate who owes who what amount of money, and generate reports to help reconcile the accounts.

## Features
The Group Payment Tracker application consists of the following features:
- Member page: Allows members to create an account and join the group
- Deposit page: Allows members to record expenses paid to vendors, restaurants or any other service provider
- Internal Payment page: Allows members to record payments made to other members of the group
- Report page: Allows members to view their balances and generate reports to help reconcile the accounts

## Requirements
The project requires the following dependencies to be installed:
- Python 3.x
- Django 3.x
- SQLite database

## Installation
To install and run the project on your local machine, follow these steps:
1. Clone the project repository from GitHub: `git clone https://github.com/YGourarie/ledger_project`
2. Install the dependencies by running `pip install -r requirements.txt`
3. Create a local SQLite database by running `python manage.py migrate`
4. Start the development server by running `python manage.py runserver`
5. Navigate to `http://localhost:8000` in your browser to access the application

## Usage
Once you have the application up and running, you can start using the different features of the application by following these steps:
1. Create members by navigating to the member page and filling out the form
2. Record deposits by navigating to the deposit page and filling out the form
3. Record internal payments by navigating to the internal payment page and filling out the form
4. Generate reports by navigating to the report page and selecting the relevant options

