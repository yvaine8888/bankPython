import unittest
from main import* 

class MyTests(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(check_balance(635212), 15)
    
    def test_deposit(self):
        self.assertTrue(deposit(621351, 30))

    def test_withdraw(self):
        self.assertTrue(withdraw(621351, 30))

    def test_delete(self):
        self.assertTrue(delete(277358))

if __name__ == '__main__':
    unittest.main()