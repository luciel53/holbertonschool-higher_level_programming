#!/usr/bin/python3
"""Unittest for Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittest for Square"""
    def test_to_dictionary(self):
        """
        Test of to_dictionary() in Square exists
        """
        dict = {'id': 7, 'size': 10, 'x': 9, 'y': 8}
        s = Square(10, 9, 8, 7)
        self.assertEqual(dict, s.to_dictionary())

    def test_save_to_file(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual("[]", file.read())


if __name__ == "__main__":
    unittest.main()
