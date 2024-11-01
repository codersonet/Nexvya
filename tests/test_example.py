# test/test_example.py

import unittest

class TestExample(unittest.TestCase):
    def test_basic_functionality(self):
        """Test that True is True."""
        self.assertTrue(True)  # A basic assertion to verify that everything is set up correctly

if __name__ == '__main__':
    unittest.main()  # Run the tests
