import unittest
from main import* 
from unittest.mock import patch

class MyTests(unittest.TestCase):
    def a_delete(self):
        self.assertTrue(delete(316184))
    
    def b_create(self):
        self.assertTrue(create('bliew', 15, 316184))

    def c_balance(self):
        self.assertEqual(check_balance('bliew'), {316184: 15})
    
    def d_deposit(self):
        self.assertTrue(change_balance(316184, 30))

    def e_withdraw(self):
        self.assertTrue(change_balance(316184, -30))
    
    def f_modify_name():
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['name', 'Yvaine', 'N']
            result = modify('bliew')
            self.assertEqual(result, 'bliew')

    def g_modify_name():
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['name', 'Bethany', 'Y', 'name', 'Bethany', 'N']
            result = modify('bliew')
            self.assertEqual(result, 'bliew')

    def g_modify_username():
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['username', 'yliew', 'Y', 'username', 'bliew', 'N']
            result = modify('bliew')
            self.assertEqual(result, 'bliew')
    
    def g_modify_password():
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ['password', '456', 'Y', 'password', '123', 'N']
            result = modify('bliew')
            self.assertEqual(result, 'bliew')


if __name__ == '__main__':
    unittest.main()