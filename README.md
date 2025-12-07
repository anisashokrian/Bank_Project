🏦 Bank Management System

A simple banking management application built with Python, Tkinter, SQLite, and the MVC architecture.
This project was developed individually.

📋 Table of Contents

Features

Architecture

Technologies Used

Installation

Usage

Project Structure

Modules

Contribution

License

Acknowledgments

✨ Features

Core Functions

Open Account 

Fields: id, name, password, cash_deposit

Deposit 

Fields: id, cash

Withdraw 

Fields: id, cash, password

User Interface

Built with Tkinter

Clean and simple layout

Table component for displaying data

Reusable UI components (LabelWithEntry, Table)

Data Management

SQLite database

Input validation

Repository layer for database interaction

Test data included

🏗 Architecture

The project follows the MVC (Model–View–Controller) architecture:
View → Controller → Repository → Database 

🛠 Technologies Used

Language: Python 3.x

GUI Framework: Tkinter

Database: SQLite

Architecture: MVC

Testing: unittest

📦 Installation

Requirements

Python 3.7+

pip package manager

Steps

Clone the repository

git clone https://github.com/yourusername/Bank_Project.git cd Bank_Project 

Install dependencies (if any)

pip install -r requirements.txt 

Initialize the database
The database creates automatically on first run.
Or manually:

sqlite3 bank.sqlite < db/database_tables.sql sqlite3 bank.sqlite < db/test_data.sql 

Run the application

python bank_main.py 

🚀 Usage

Start Application

python bank_main.py 

Operations

Open Account – create a new bank account

Deposit – add money using ID

Withdraw – withdraw money using ID and password

All views contain:

Save

Update

Delete

Refresh

Input validation

📁 Project Structure

Bank_project/ │ ├── bank_main.py ├── bank.sqlite │ ├── controller/ │ ├── init.py │ ├── open_account_controller.py │ ├── deposit_controller.py │ └── withdraw_controller.py │ ├── model/ │ ├── init.py │ ├── bank_model.py │ ├── open_account.py │ ├── deposit.py │ └── withdraw.py │ ├── repository/ │ ├── init.py │ ├── open_account_repository.py │ ├── deposit_repository.py │ └── withdraw_repository.py │ ├── view/ │ ├── init.py │ ├── bank_view.py │ ├── open_account_view.py │ ├── deposit_view.py │ ├── withdraw_view.py │ │ │ └── component/ │ ├── init.py │ ├── label_with_entry.py │ └── table.py │ ├── db/ │ ├── init.py │ ├── database_tables.sql │ └── test_data.sql │ └── test/ ├── init.py ├── open_account_test.py ├── deposit_test.py └── withdraw_test.py 

📚 Modules

Entities

OpenAccount – create account

Deposit – deposit money

Withdraw – withdraw money

UI Components

LabelWithEntry – reusable input component

Table – custom table built with Treeview

👥 Contribution

Fork the repository

Create a feature branch (git checkout -b feature/FeatureName)

Commit changes (git commit -m "Add FeatureName")

Push and open a Pull Request

📄 License

This project is licensed under the MIT License.

🙏 Acknowledgments

Special thanks to my instructor for guidance and support during development.
