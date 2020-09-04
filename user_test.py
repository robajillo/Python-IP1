import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    def setUp(self)
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("robajillo", "robajillo2020")  # Created new user
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.user_name, "robajillo")
        self.assertEqual(self.new_user.password, "robajillo2020")

    def test_save_user(self):
        '''
        check if user information can be saved to the user user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        check if you can save multiple user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","password")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
