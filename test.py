import unittest
from main import* 
from unittest.mock import patch

class MyTests(unittest.TestCase):
    def test_adelete(self):
        self.assertTrue(delete(316184, 'bliew'))
    
    def test_bcreate(self):
        self.assertTrue(create('bliew', 15, 316184))

    def test_cbalance(self):
        self.assertEqual(check_balance('bliew', 'User'), {316184: 15})
    
    def test_deposit(self):
        self.assertTrue(change_balance(316184, 30, False, 'bliew'))

    def test_ewithdraw(self):
        self.assertTrue(change_balance(316184, -30, True, 'bliew'))
    
    def test_fmodify_name(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['name', 'Yvaine', 'N']
            result = modify('bliew', 'User')
            self.assertEqual(result, 'bliew')

    def test_modify_name(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['name', 'Bethany', 'Y', 'name', 'Bethany', 'N']
            result = modify('bliew', 'User')
            self.assertEqual(result, 'bliew')

    def test_modify_username(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['username', 'tliew', 'Y', 'username', 'bliew', 'N']
            result = modify('bliew', 'User')
            self.assertEqual(result, 'bliew')
    
    def test_modify_password(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['password', '456', 'Y', 'password', '123', 'N']
            result = modify('bliew', 'User')
            self.assertEqual(result, 'bliew')


if __name__ == '__main__':
    unittest.main()