import unittest
from controller.withdraw_controller import WithdrawController


class TestWithdrawController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = WithdrawController()

    def test_save_bank(self):
        """Test saving a bank"""
        status, message = self.controller.withdraw( 10, 6612,"anisa1234")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)
