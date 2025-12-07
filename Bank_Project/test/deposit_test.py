import unittest
from controller.deposit_controller import DepositController

class TestDepositController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = DepositController

    def test_save_bank(self):
        """Test saving a bank"""
        status, message = self.controller.deposit( 10, 6612)
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)
