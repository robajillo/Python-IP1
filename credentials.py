import pyperclip
import string
import random
class Credentials:
    '''
    class that creates instances of user accounts
    '''
    credentials_list = []

    def __init__(self, account , email , password):
        self.account = account 
        self.email = email
        self.password = password

    def save_credentials(self):
        '''
        self credentials in credentials_list
        '''
        Credentials.credentials_list.append(self)  
    def generate_password(size=10) : 
        '''
		method to generate 10 character password for a credential
		'''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~`!@#$%^&*()_-+=[{]}'\|?/>.,<"
        gen_pass =''.join(random.choice(password) for i in range(size))
        return gen_pass  
    

    def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentials_list.remove(self)   

    @classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials   
    @classmethod
    def credentials_exists(cls, account):
        '''
        confirm a class exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
        return False   

    @classmethod
    def display_credentials(cls):
        '''
        method that returns all credentials
        '''
        return cls.credentials_list

    