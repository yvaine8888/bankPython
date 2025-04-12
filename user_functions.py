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