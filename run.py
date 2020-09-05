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
