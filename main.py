import mysql.connector
import random

def check_balance(num):
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('SELECT * FROM the_users WHERE Account = %s')
    cursor.execute(query, (num,))
    found = cursor.fetchone()
    balance = found[4]
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
    found = cursor.fetchone()
    amount = found[4] + amount
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
    found = cursor.fetchone()
    amount = found[4] - amount
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

def modify(num):
    while True:
        changing = input("What would you like to change? name/pin: ")
        if changing == "name":
            name = input("Please enter your new name: ")
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('UPDATE the_users SET Name = %s WHERE Account = %s')
            cursor.execute(query, (name, num))
            connection.commit()
            cursor.close()
            connection.close()
            print("You have successfully changed your name.")
        elif changing == "signup":
            pin_num = input("Please enter your new PIN: ")
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('UPDATE the_users SET PIN = %s WHERE Account = %s')
            cursor.execute(query, (pin_num, num))
            connection.commit()
            cursor.close()
            connection.close()
            print("You have successfully changed your PIN.")
        else:
            print("Please enter name or pin next time.")
            continue
        proceed = input("Do you want to change anything else? Y/N: ")
        if proceed == "N":
            break
        
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
                found = cursor.fetchone()
                if found != None:
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
            print("Congratulations! You have made an account.")
            print(f"Your account number is {account_num}.")
            return account_num
        else:
            print("Please enter login or signup next time.")

def menu():
    print("\n---------Menu---------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Delete Account")
    print("5. Modify Account")
    print("6. Log out")
    print("----------------------")

def main():
    while True:
        print("Welcome to this online banking system!")
        account = logging_in()
        print("\nWhat would you like to do?")
        while True:
            menu()
            num = int(input("Please choose a number 1-6: "))
            print()
            if num == 1:
                check_balance(account)
            elif num == 2:
                deposit(account)
            elif num == 3:
                withdraw(account)
            elif num == 4:
                delete(account)
            elif num == 5:
                modify(account)
            elif num == 6:
                break
            else:
                print("Please choose a number 1-6 next time.")
    

if __name__ == "__main__":
    main()