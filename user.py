class User:

    '''
    class that generates new instance of user
    '''

    user_list = []

    def __init__ (self, user_name, password):
        self.user_name = user_name

        self.password = password
    def save_user(self):
         User.user_list.append(self)

    def delete_user(self):
        '''
        delete user account
        '''
        User.user_list.remove(self)   
    @classmethod
    def find_user(cls,user_name):
        '''
        finding username
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def log_in(cls,user_name, password):
        '''
        login to password locker
        '''
        for user in cls.user_list:
            if user.user_name == user_name and user.password == user_password:
                return user

    @classmethod
    def display_user(cls):
        '''
        Method that returns the user list
        '''
        
        return cls.user_list