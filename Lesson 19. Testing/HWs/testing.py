import unittest
from bank import Bank, SavingsAccount, CurrentAccount
from unittest.mock import patch

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
    
    def test_open_account(self):
        balance = 1000
        account_number = "001"
        interest = 2.5
        savings = SavingsAccount(balance, account_number, interest)
        self.bank.open_account(savings)

        self.assertEqual(savings.get_balance(), balance, "No balance in the account")
        self.assertIn(savings, self.bank.accounts, "No such account in bank")

    @patch("builtins.print")
    def test_update(self, mock_print):
        balance = -400
        account_number = "002"
        overdraft_limit = -300
        current = CurrentAccount(balance, account_number, overdraft_limit)
        self.bank.open_account(current)
        self.bank.update()
        
        mock_print.assert_called_once_with("Overdraft letter sent for Account 002")    

unittest.main()
    