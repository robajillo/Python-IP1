import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    def setUp(self):
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
        test_user = User("Test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test if one can remove user account
        '''
        self.new_user.save_user()
        test_user = User("Test", "password")  #new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("Test", "password")
        test_user.save_user()
        found_user = User.find_user("robajillo")
        self.assertEqual(found_user.user_name, self.new_user.user_name)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(), user.user_list)


if __name__ == '__main__':
    unittest.main()
