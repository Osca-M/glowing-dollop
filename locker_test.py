import unittest
from locker import User ,Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.user = User('WangechiKimani','123Pass')
        self.credentials =Credentials('instagram','WangechiKimani','123Pass')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.user.username,'WangechiKimani')
        self.assertEqual(self.user.password,'123Pass')

     def test_save_user(self):
         """
        test case to test if a new user instance has been saved into the User list

        """
        self.user.save_user()
        self.assertGreater(len(User.user_list),0)

         def test_get_user(self):
        self.user.save_user()
        self.assertIsNot(User.get_user(User('WangechiKimani', '123Pass')), False)

    def test_save_credentials(self):
        self.credentials.save_credential()
        self.assertGreater(len(Credentials.credentials_list), 0)

    def test_generate_random_password_with_predefined_length(self):
        credentials = Credentials('twitter', 'WangechiKimani')
        password = credentials.generate_random_password(2)
        self.assertEqual(len(password), 2)

    def test_generate_random_password_with_standard_length(self):
        credentials = Credentials('twitter', 'WangechiKimani')
        password = credentials.generate_random_password()
        self.assertEqual(len(password), 10)

    def test_find_credentials(self):
        self.credentials.save_credential()
        self.assertEqual(len(self.user.find_credentials()), 0)


     def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","WangechiKimani","456Pass") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

      def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","mikeycharles","Mfh45hfk")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
   
    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","mikeycharles","Mfh45hfk") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)

if __name__ == "__main__":
    unittest.main()
