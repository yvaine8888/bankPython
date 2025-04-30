import mysql.connector
import random
import time

# Checking the balances of all accounts and returning it as a dictionary
def check_balance(username, status):
    result = {}
    
    # Get the account and its balance
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    if status == "Admin":
        query = ('SELECT * FROM account_info')
        cursor.execute(query)
    else:
        query = ('SELECT * FROM account_info WHERE Name = %s')
        cursor.execute(query, (username,))

    # Adding to dictionary
    found = cursor.fetchall()
    for item in found:
        result[item[2]] = item[3]
    cursor.close()
    connection.close()
    return result

# Getting a unique account number
def unique_number():
    num = 0
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    # Get random numbers until it is unique
    while True:
        num = random.randint(100000, 999999)
        query = ('SELECT * FROM account_info WHERE Account = %s')
        cursor.execute(query, (num,))
        if cursor.fetchone() == None:
            break
    cursor.close()
    connection.close()
    return num
    
# Creating an account
def create(username, amount, account):
    # Getting an unique account number
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('INSERT INTO account_info (Name, Account, Balance) VALUES (%s, %s, %s)')
    record = (username, account, float(amount))
    cursor.execute(query, record)
    connection.commit()
    
    # Checking if it is there
    query = ('SELECT * FROM account_info WHERE Account = %s')
    cursor.execute(query, (account,))
    found = cursor.fetchone()
    cursor.close()
    connection.close()
    if found != None:
        return True
    else:
        return False

# Changing the balance of a given account
def change_balance(num, amount, withdraw, username):
    result = 0

    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()

    # Find balance and get the resulting one
    if withdraw:
        query = ('SELECT * FROM account_info WHERE Account = %s AND Name = %s')
        cursor.execute(query, (num, username))
    else:
        query = ('SELECT * FROM account_info WHERE Account = %s')
        cursor.execute(query, (num,))

    found = cursor.fetchone()
    if found != None:
        result = amount + found[3]
    else:
        cursor.close()
        connection.close()
        return False

    # Update it
    query = ('UPDATE account_info SET Balance = %s WHERE Account = %s')
    cursor.execute(query, (result, num))
    connection.commit()

    cursor.close()
    connection.close()
    return True

# Deleting an account
def delete(num, username):
    # Deleting it
    connection = mysql.connector.connect(user = "root", database = "example", 
    password = "x1321PF@33")
    cursor = connection.cursor()
    query = ('DELETE FROM account_info WHERE Account = %s')
    cursor.execute(query, (num,))
    connection.commit()
    # Checking if it is still there
    query = ('SELECT * FROM account_info WHERE Account = %s')
    cursor.execute(query, (num,))
    found = cursor.fetchone()
    cursor.close()
    connection.close()
    if found == None:
        return True
    else:
        return False

# Modifying an account
def modify(the_username, status):
    while True:
        username = the_username
        # Seeing if admin. They can change any account.
        if status == "Admin":
            while True:
                username = input("Whose account would you like to change? Please enter their username: ")
                connection = mysql.connector.connect(user = "root", database = "example", 
                password = "x1321PF@33")
                cursor = connection.cursor()
                query = ('SELECT * FROM login_info WHERE Username = %s')
                cursor.execute(query, (username,))
                found = cursor.fetchone()
                cursor.close()
                connection.close()
                if found != None:
                    break
                
        changing = input("What would you like to change? username/name/password: ")

        # Changing the name
        if changing == "name":
            name = input("Please enter your new name: ")
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('UPDATE login_info SET Name = %s WHERE Username = %s')
            cursor.execute(query, (name, username))
            connection.commit()
            cursor.close()
            connection.close()
            print("You have successfully changed the name.")
        # Changing the password
        elif changing == "password":
            pin = input("Please enter your new password: ")
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('UPDATE login_info SET Password = %s WHERE Username = %s')
            cursor.execute(query, (pin, username))
            connection.commit()
            cursor.close()
            connection.close()
            print("You have successfully changed your password.")
        # Changing the username which also needs to be unique
        elif changing == "username":
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()

            # Getting a unique username
            while True:
                name = input("Please enter your new username: ")
                query = ('SELECT * FROM login_info WHERE Username = %s')
                cursor.execute(query, (name,))
                found = cursor.fetchone()
                if found == None:
                    break 
                print("There is already a username like that.")
            # Changing it
            query = ('UPDATE login_info SET Username = %s WHERE Username = %s')
            cursor.execute(query, (name, username))
            query = ('UPDATE account_info SET Name = %s WHERE Name = %s')
            cursor.execute(query, (name, username))
            if the_username == username:
                the_username = name
            connection.commit()
            cursor.close()
            connection.close()
            print("You have successfully changed your username.")
        else:
            print("Please enter username, name, or password next time.")
            continue
        # See if they want to change anything else
        proceed = input("\nDo you want to change anything else? Y/N: ")
        if proceed == "N":
            return the_username
        
def logging_in():
    login_type = input("Do you want to log in or create an account? (login/signup): ")
    print()
    while True:
        if login_type == "login":
            # Getting login info
            username = input("Please enter your username: ")
            pwd = input("Please enter your password: ")
            
            # Seeing if the login info is there
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('SELECT * FROM login_info WHERE Username = %s AND Password = %s')
            cursor.execute(query, (username, pwd))
            found = cursor.fetchone()

            # If there is break but if not, print error
            if found != None:
                cursor.close()
                connection.close()
                message = f"Welcome back, {found[4]} {found[3]}!"
                return username, message, found[4]
            else:
                print("There is something wrong with the username or password. Please try again.")

            cursor.close()
            connection.close()

        elif login_type == "signup":
            # Getting login info
            name = input("Please enter your name: ")
            username = input("Please enter your username: ")

            # Seeing if there is already a user name like it
            connection = mysql.connector.connect(user = "root", database = "example", 
            password = "x1321PF@33")
            cursor = connection.cursor()
            query = ('SELECT * FROM login_info WHERE Username = %s')
            cursor.execute(query, (username,))
            found = cursor.fetchone()
            # Bringing back to start if there is
            if found != None:
                cursor.close()
                connection.close()
                continue

            pwd = input("Please enter your password: ")

            # Inserting login info if there isn't
            query = ('INSERT INTO login_info (Username, Password, Name, Status) VALUES (%s, %s, %s, %s)')
            record = (username, pwd, name, "User")
            cursor.execute(query, record)
            connection.commit()
            cursor.close()
            connection.close()

            # Printing result and returning username and a message 
            print("Congratulations! You have made an account.")
            message = f"Welcome new User, {name}!"
            return username, message, "User"
        else:
            print("Please enter login or signup next time.")

def menu():
    print("\n---------Menu---------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create Account")
    print("5. Delete Account")
    print("6. Modify Your Account")
    print("7. Log out")
    print("----------------------")

def main():
    while True:
        # Welcome
        print("Welcome to this online banking system!")
        username, message, status = logging_in()
        print("\n" + message)
        print("\nWhat would you like to do?")
        time.sleep(1)
        menu()
        
        # User functions
        while True:
            try:
                num = int(input("Please choose a number 1-7: "))
            except ValueError:
                num = 0
            print()
            
            if num == 1:
                result = check_balance(username, status)
                for key, value in result.items():
                    print(f"Account {key} - ${value}")

            elif num == 2:
                try:
                    account = int(input("What is the account numnber?: "))
                    amount = float(input("How much would you like to deposit?: "))
                    if change_balance(account, amount, False, username):
                        print(f"Successfully deposited ${amount}.")
                    else:
                        print(f"Failed to deposit ${amount}.")
                except ValueError:
                    print("Please enter numbers next time.")

            elif num == 3:
                try:
                    account = int(input("What is the account numnber?: "))
                    amount = float(input("How much would you like to withdraw?: "))
                    if change_balance(account, amount * -1, True, username):
                        print(f"Successfully withdrew ${amount}.")
                    else:
                        print(f"Failed to withdraw ${amount}.")
                except ValueError:
                    print("Please enter numbers next time.")

            elif num == 4:
                try:
                    amount = float(input("What is the principal amount?: "))
                    account = unique_number()
                    if create(username, amount, account):
                        print("Successfully created an account.")
                        print(f"Your account number is {account}")
                    else:
                        print("Failed to create an account")
                except ValueError:
                    print("Please enter numbers next time.")
        
            elif num == 5:
                try:
                    account = int(input("What is the account you want to delete?: "))
                    proceed = input("Are you sure you want to delete this account? Y/N: ")
                    if proceed == "Y":
                        if delete(account, username):
                            print("Successfully deleted your account.")
                        else:
                            print("Failed to delete your account.")
                except ValueError:
                    print("Please enter numbers next time.")
            elif num == 6:
                username = modify(username, status)
            elif num == 7:
                print("Thank you for using this system!")
                print("Have a great day!\n")
                break
            else:
                print("Please choose a number 1-7 next time.")
            time.sleep(2)
            menu()
    

if __name__ == "__main__":
    main()