import project
import unittest
from unittest.mock import patch, call

class TestCheckPassword(unittest.TestCase):
    
    @patch('builtins.input', side_effect =['short', 'noNumbers!', 'validPass1'])
    def test_check_password(self, mock_input):
        initial_password = 'badpass'
        
        result = project.check_password(initial_password)
        
        # Check that the function eventually returns the valid password
        self.assertEqual(result, 'validPass1')
        
        # Check that the input function was called three times
        self.assertEqual(mock_input.call_count, 3)

        mock_input.assert_has_calls([
            call("Re-enter password: "),
            call("Re-enter password: "),
            call("Re-enter password: ")
        ])
        assert project.check_password("helloworld1") == "helloworld1"
        assert project.check_password("validpassword1") == "validpassword1"



class TestCheckEmail(unittest.TestCase):
    def setUp(self):
        self.email_password = {
            'test@example.com': 'password123',
            'user@example.com': 'mysecretpassword',
        }

    @patch('builtins.input', side_effect=['test@example.com', 'newuser@example.com'])
    def test_check_email_existing_then_new(self, mock_input):
        result = project.check_email('test@example.com', self.email_password)
        self.assertEqual(result, 'newuser@example.com')

    @patch('builtins.input', side_effect=['invalidemail', 'anotherinvalidemail', 'valid@example.com'])
    def test_check_email_invalid_then_valid(self, mock_input):
        result = project.check_email('invalidemail', self.email_password)
        self.assertEqual(result, 'valid@example.com')

    @patch('builtins.input', side_effect=['user@example.com', 'alsoinvalid', 'valid@example.com'])
    def test_check_email_existing_and_invalid_then_valid(self, mock_input):
        result = project.check_email('user@example.com', self.email_password)
        self.assertEqual(result, 'valid@example.com')


class TestConfirmPassword(unittest.TestCase):
    def setUp(self):
        self.accounts = {
            'user1': 'password123',
            'user2': 'mysecretpassword',
        }

    @patch('builtins.input', side_effect=['wrongpassword', 'anotherwrongpassword', 'password123'])
    def test_confirm_password_success(self, mock_input):
        self.assertTrue(project.confirm_password('wrongpassword', 'user1', self.accounts))

    @patch('builtins.input', side_effect=['wrongpassword', 'mysecretpassword'])
    def test_confirm_password_success_with_user2(self, mock_input):
        self.assertTrue(project.confirm_password('wrongpassword', 'user2', self.accounts))


if __name__ == "__main__":
    unittest.main()