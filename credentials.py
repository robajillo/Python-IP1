import pyperclip
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