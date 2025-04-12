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