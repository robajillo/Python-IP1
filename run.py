#!/usr/bin/env python3.8
import random
from credentials import Credentials
from user import User

def create_user(user_name,password):
    '''
    method to create user account
    '''

    new_user = User(user_name,password)

    return new_user
def save_user(user):
    '''
    method to save account
    '''
    user.save_user()  
def save_credentials(credentials):
    '''
    method to save credentials account
    '''
    credentials.save_credentials

def find_user (user_name):
    '''
    method for finding user using user_name
    '''
    return User.find_user(user_name)

def create_credentials(account, email, password):
    '''
    method to create credentials
    '''
    new_credentials = Credentials(account, email, password) 
    return new_credentials

def save_credentials(credentials):
    '''
    method to save credentials
    '''
    credentials.save_credentials()

def display_credentials():
    '''
    method to display all credentials
    '''
    return Credentials.display_credentials()

def find_account(account):
    '''
    method to search for account 
    '''
    return Credentials.find_account(account)   
    
def delete_credentials(account):
    '''
    method to delete account
    '''
    credentials.delete_credentials() 


def check_existing_users(user_name):
    '''
    method that checks if a user name already exists
    
    '''

    return User.user_exist(user_name)

def user_log_in(user_name, password):
    '''
    Function that allows a user to log into their credential account
    
    '''
    log_in = User.log_in(user_name, password)
    if log_in != False:
        return User.log_in(user_name, password)

def display_user():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()  

def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass


def main():
    '''
    Function running the Password Locker app
    '''
    print("Welcome to Password Locker!!! \n use the short codes to navigate through")
    print('\n')
    print("select a short code: 'nu' to create new user: 'du' to display users: 'lg' to login 'ex' to exit ")
    while True:
        '''
        loop that runs the entire application
        '''
       

        short_code = input().lower()

        if short_code == 'nu':
            '''
            creating password locker account 
            '''
            print("create username")
            created_user_name = input()
            print("create password")
            created_user_password = input()

            print('Confirm Password')
            confirm_password = input()
            save_user(create_user(created_user_name, created_user_password))


            while confirm_password != created_user_password:
                print("invalid password did not match!!!")
                print("Enter your password")
                created_user_password = input()
                print("Confirm your Password")
                confirm_password = input()
            else:
                print(f"congratulations {created_user_name}! account creation succesful")
                print("to proceed to login use short code 'lg' to display user use 'du'")
            
        elif short_code == 'du':
            '''
            displays the name of the current users
            '''
            if display_user():
                print('\n')
                print("here are the users of password locker")
                print("-"*10)

                for user in display_user():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")


        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker account
            '''
            print("\n")
            print("Log into Password Locker Account")
            print("enter username")
            created_user_name = input()
            print("enter password")
            created_user_password = input()

            print('Confirm Password')
            confirm_password = input()
            while confirm_password != created_user_password:
                print("invalid password did not match!!!")
                print("Enter your password")
                created_user_password = input()
                print("Confirm your Password")
                confirm_password = input()
            
            else:
                print("\n")
                print(f'''login was successful dear {created_user_name} welcome to your Credentials\n
                Use these short codes to get around''')
                print("cc-create credentials account dc- display credentials  ex- exit")

                
                
        elif short_code == 'cc':
            '''
            Creating a Credential
            '''

            print("\n")
            print("New Credential")
            print("-"*10)

            print("Account Name ...")
            account = input()

            print("Email ...")
            email = input()

            print("Please choose an option for entering a password: 'ep'- to enter passsword and gp - to generate password")
            password_choice = input()
            if password_choice == 'ep':
                print("enter your password...")
                password = input()
            elif password_choice == 'gp':
                password = generate_password()
                

            # Create and save new user
            save_credentials( create_credentials(  account, email, password) )

            print("\n")
            print(f"Credentials for {account} have been created and saved")
            print("\n")
            print("to display credentials use 'dc' ")
        

        elif short_code == 'dc':
            '''
            Displaying credential name and password
            '''

            if display_credentials():
                print("\n")
                print(f"{account}'s credentials")
                print("-"*10)

                for credentials in display_credentials():
                    print(f"Account ..... {credentials.account}")
                    print(f"Email......{credentials.email}")
                    print(f"Password .... {credentials.password}")
                    print("-"*10)
                    print("to delete credentials use 'de' ")

            else:
                print("\n")
                print("You have no credentials")
                print("\n")

       
        elif short_code == 'de': 
            print("Enter the account name of the Credentials you want to delete")
            find_credentials = input()
            if find_account(find_credentials):
                result = find_account(find_credentials)
                print("_"*50)
                result.delete_credentials()
                print('\n')
                print(f"Your stored credentials  successfully deleted!!!")
                


        

        
        
            
        elif short_code == 'ex':
             break
        else:
            print("enter valid code to continue")



if __name__ == '__main__':

    main()




    

