import mysql.connector
import random

def logging_in():
    login_type = input("Do you want to log in or create an account? (login/signup): ")
    while True:
        if login_type == "login":
            account_num = input("Please enter your account number: ")
            pin_num = input("Please enter your PIN: ")
            try:
                okay = False
                x = int(account_num)

                connection = mysql.connector.connect(user = "root", database = "example", 
                password = "x1321PF@33")
                cursor = connection.cursor()
                query = ('SELECT * FROM the_users WHERE Account = %s AND PIN = %s')
                cursor.execute(query, (account_num, pin_num))
                row = cursor.fetchone()
                if row != None:
                    okay = True
                else:
                    print("There is something wrong. Please try again.")

                cursor.close()
                connection.close()
                if okay:
                    return account_num

            except ValueError:
                print("Please enter numbers for the account.")
        elif login_type == "signup":
            username = input("Please enter your name: ")
            user_pin = input("Please enter your PIN: ")
            account_num = random.randint(100000, 999999)

            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('INSERT INTO the_users (Name, Account, PIN, Balance) VALUES (%s, %s, %s, %s)')
            record = (username, account_num, user_pin, 0)
            cursor.execute(query, record)
            connection.commit()
            cursor.close()
            connection.close()

            return account_num
        else:
            print("Please enter login or signup next time.")

def menu():
    print("---------Menu---------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Delete Account")
    print("5. Modify Account")
    print("----------------------")

def check_balance(num):
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('SELECT * FROM the_users WHERE Account = %s')
    cursor.execute(query, (num,))
    balance = cursor[0][4]
    print(f"You have ${balance} in your account.")
    cursor.close()
    connection.close()

def deposit(num):
    amount = int(input("How much would you like to deposit?: "))
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('SELECT * FROM the_users WHERE Account = %s')
    cursor.execute(query, (num,))
    row = cursor.fetchone()
    amount = row[4] + amount
    query = ('UPDATE the_users SET Balance = %s WHERE Account = %s')
    cursor.execute(query, (amount, num))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Successfully deposited ${amount}.")

def withdraw(num):
    amount = int(input("How much would you like to withdraw?: "))
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('SELECT * FROM the_users WHERE Account = %s')
    cursor.execute(query, (num,))
    row = cursor.fetchone()
    amount = row[4] - amount
    query = ('UPDATE the_users SET Balance = %s WHERE Account = %s')
    cursor.execute(query, (amount, num))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Successfully withdrew ${amount}.")

def delete(num):
    proceed = input("Are you sure you want to delete your account? Y/N: ")
    if proceed == "Y":
        connection = mysql.connector.connect(user = "root", database = "example", 
        password = "x1321PF@33")
        cursor = connection.cursor()
        query = ('DELETE FROM the_users WHERE Account = %s')
        cursor.execute(query, (num,))
        connection.commit()
        cursor.close()
        connection.close()

def main():
    print("Welcome to this online banking system!")
    account = logging_in()
    print("What would you like to do?")
    menu()
    num = int(input("Please choose a number 1-5: "))

    if num == 1:
        check_balance(account)
    elif num == 2:
        deposit(account)
    elif num == 3:
        withdraw(account)
    elif num == 4:
        delete(account)
    elif num == 5:
        print("modify(account)")
    

if __name__ == "__main__":
    main()