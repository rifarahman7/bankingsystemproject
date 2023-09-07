# bankingsystemproject
This is a simple banking system script that allows users to log in with their account number and PIN. Once logged in, users can perform various banking operations such as depositing, withdrawing, and checking their account balance. The account information and balances are stored in a MySQL database named 'proj'. Let's go through the code step by step:

Importing the necessary libraries:

The code begins with importing the mysql.connector library to interact with the MySQL database.
BankAccount class:

This class represents a bank account and has attributes: account_no, pin, and balance.
The login method checks whether the provided account number and PIN match the stored values.
The deposit method allows users to deposit a positive amount, and it updates the balance in the database.
The withdraw method allows users to withdraw a positive amount, given that their balance is sufficient. It also updates the balance in the database.
The update_balance_in_database method is a private method that connects to the database and updates the balance.
main function:

The main function is the entry point 
It asks the user to input their account number and PIN to log in.
The provided credentials are checked against the database.
If the login is successful, a BankAccount object is created, and the user is presented with a menu to choose from various operations.
The user can deposit, withdraw, check balance, or exit the program.
