#!/usr/bin/python3

"""
./test_loop_float_python.py -v
"""

import unittest
from loop_float_python import loop_count_add

class Testloop_count_add_From1_To100(unittest.TestCase):
    """
    """

    def test_loop_count_add(self):
        """
        """
        value1 = 1
        value2 = 100
        value3 = 1
        value4 = 1

        expected = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                     51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
                     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                     71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
                     81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
                     91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]

        actual = loop_count_add(value1, value2, value3, value4)
        self.assertEqual(expected, actual)

class Testloop_count_add_From0_01_To1(unittest.TestCase):
    """
    """

    def test_loop_count_add(self):
        """
        """
        value1 = 1
        value2 = 100
        value3 = 1
        value4 = 1
        #value3 = 0.01
        #value4 = 0.01

        expected = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                     51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
                     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                     71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
                     81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
                     91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]

        actual = loop_count_add(value1, value2, value3, value4)
        self.assertEqual(expected, actual)

if __name__ == "__main__":

    unittest.main()
