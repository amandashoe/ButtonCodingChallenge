"""
Unit test for module button

When run as a script, this module invokes several procedures that 
test the function expEval() in the module button.

Amanda Xu
3/20/18
"""
import button
import unittest

class Test(unittest.TestCase):
    """
    A class that contains a testing method for the function expEval()
    
    This class is a subclass of TestCase.
    """
    def test_expEval(self):
        """Tests various cases for function expEval()"""
        self.assertEqual(6, button.expEval("+ 1 + 2 3"))
        self.assertEqual(-1, button.expEval("- 5 + 1 + 2 3"))
        self.assertEqual(2, button.expEval("- 1 - 2 3"))
        self.assertEqual(11, button.expEval("- 1 - 10 20"))
        self.assertEqual(0, button.expEval("- 0 0"))
        self.assertEqual(0, button.expEval("+ 0 0"))
        with self.assertRaises(AssertionError):
            button.expEval("")
        with self.assertRaises(AssertionError):
            button.expEval(3)

if __name__ == '__main__':
    unittest.main()

