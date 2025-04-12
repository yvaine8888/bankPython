import mysql.connector
import random
from user_functions import *
from features import *

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