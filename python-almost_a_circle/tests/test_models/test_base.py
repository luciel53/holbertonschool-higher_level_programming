#!/usr/bin/python3
import unittest
from models.square import Square


class TestBase_save_to_file(unittest.TestCase):
    """Unittest to test save_to_file medthod"""
    def test_save_to_file(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        with open("Square.json", 'r') as file:
            self.assertEqual("[]", file.read())

if __name__ == "__main__":
    unittest.main()
