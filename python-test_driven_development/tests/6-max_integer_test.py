#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_no_list(self):
        # Test empty list
        self.assertEqual(max_integer(""), None)

    def test_one_element(self):
        #test for only one element
        elem = [2]
        self.assertEqual(max_integer(elem), 2)

    def test_all_negative_numb(self):
        #test for only negative numbers in a list
        neg_numb = [-5, -7, -3, -1]
        self.assertEqual(max_integer(neg_numb), -1)

    def test_one_negative_numb(self):
        one_neg_numb = [8, -9, 3, 5]
        self.assertEqual(max_integer(one_neg_numb), 8)

