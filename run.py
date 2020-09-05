from credentials import Credentials
from user import User

def create_user(name,password):
    '''
    method to create new account
    '''

    new_user = User(name,password)

    return new_user
def save_users(user):
    '''
    method to save account
    '''
    user.save_user()  
def      