import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_credentials = Credentials ("Yahoo","roba@yahoo.com","yahoo2020")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    def test__init(self):
        '''
        check if instance is initialiazing as expected
        '''
        self.assertEqual(self.new_credentials.account, "Yahoo")
        self.assertEqual(self.new_credentials.email, "roba@yahoo.com")
        self.assertEqual(self.new_credentials.password, "yahoo2020")

    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_saving_multiple_credentials(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Yahoo", "testuser","password")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Yahoo", "testuser","password")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_search_for_credentials(self):
        '''
        test if credentials can be searched for
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Yahoo", "testuser","password")
        test_credentials.save_credentials()
        find_credentials= Credentials.find_account("Yahoo")
        self.assertEqual(find_credentials.account, test_credentials.account)

    def test_confirm_credentials_exists(self):
        '''
        confirm that credentials exists
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Yahoo", "testuser","password")
        test_credentials.save_credentials()
        credentials_exists = Credentials.credentials_exists("Yahoo")
        self.assertTrue(credentials_exists)

if __name__ == '__main__':
    unittest.main()
       