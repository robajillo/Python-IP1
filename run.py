from credentials import Credentials
from user import User

def create_useraccount(user_name,password):
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
    new_credentials = Crendentials(account, email, password) 
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
    

    

