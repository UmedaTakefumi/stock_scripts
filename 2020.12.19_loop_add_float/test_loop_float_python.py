#!/usr/bin/python3

"""
./test_loop_float_python.py -v
"""

import unittest
from loop_float_python import * 

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

    def test_loop_count_add_decimal(self):
        """
        """
        value1 = 1
        value2 = 100
        value3 = 0.01
        value4 = 0.01

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

        ## GoogleSpreadsheet で作成... テストデータ作るのめんどい...
        expected = [ 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1,
                     0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2,
                     0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3,
                     0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4,
                     0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5,
                     0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6,
                     0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7,
                     0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8,
                     0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9,
                     0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1 ]

        actual = loop_count_add_decimal(value1, value2, value3, value4)
        self.assertEqual(expected, actual)

if __name__ == "__main__":

    unittest.main()