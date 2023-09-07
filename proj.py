import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='riF@1111',
    port='3306',
    database='proj')

import mysql.connector

class BankAccount:
    def __init__(self, account_no, pin):
        self.account_no = account_no
        self.pin = pin
        self.balance = 0

    def login(self, account_no, pin):
        return self.account_no == account_no and self.pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
            self.update_balance_in_database()
        else:
            print("Invalid amount. Please deposit a positive value.")

    def withdraw(self, amount):
        if  amount>0 :
            if amount >= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
                self.update_balance_in_database()
            else:
                print("Insufficient balance.")

    def update_balance_in_database(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='riF@1111',
            port='3306',
            database='proj'
        )
        cursor = connection.cursor()

        query = "UPDATE bank SET balance = %s WHERE account_no = %s"
        data = (self.balance, self.account_no)
        cursor.execute(query, data)

        connection.commit()
        cursor.close()
        connection.close()

def main():
    account_no = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    # Check login credentials
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='riF@1111',
        port='3306',
        database='proj'
    )
    cursor = connection.cursor()

    query = "SELECT * FROM bank WHERE account_no = %s AND pin = %s"
    data = (account_no, pin)
    cursor.execute(query, data)

    account_data = cursor.fetchone()
    cursor.close()
    connection.close()

    if account_data:
        account = BankAccount(account_no, pin)
        print("Login successful!")
        fname = account_data[1]
        print(f"Welcome, {fname}!")
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                print(f"Your current balance is: {account.balance}")
            elif choice == "4":
                print("Thank you for using our banking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Login failed. Please check your account number and PIN.")

if __name__ == "__main__":
    main()



