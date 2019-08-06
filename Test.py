# *********************************************************************************************
# Purpose: To create a Test program to check Balanced Parenthesis.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************

import unittest
from Balanced_Paranthesis import balanced


class BalancedPar(unittest.TestCase):

    def testBalanced(self):
        result = balanced("(5+6)∗(7-3)")
        expected = True
        self.assertEqual(result, expected)

    def testNotBalanced(self):
        result = balanced('(5+6)∗(7-3))')
        expected = True
        self.assertNotEqual(result, expected)


if __name__ == '__main__':
    unittest.main()