import unittest

from controller.open_account_controller import OpenAccountController


class TestOpenAccountController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = OpenAccountController

    def test_save_bank(self):
        """Test saving a bank"""
        status, message = self.controller.save("111", "saving", "an1000000", "1000")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)
