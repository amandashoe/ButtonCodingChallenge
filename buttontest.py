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
        self.assertEqual(4, button.expEval("4")) #number as expression
        self.assertEqual(-4, button.expEval("-4")) #negative int
        self.assertEqual(4, button.expEval("+4")) #redundant "+"
        self.assertEqual(5, button.expEval("+ 1 4")) #operator expression
        self.assertEqual(-3, button.expEval("+ 1 -4")) #operator expression with neg int
        self.assertEqual(5, button.expEval("+ 1 +4")) #redundant "+"
        self.assertEqual(0, button.expEval("- 0 0")) 
        self.assertEqual(0, button.expEval("+ 0 0"))
        self.assertEqual(6, button.expEval("+ 1 + 2 3")) #nested operator expressions
        self.assertEqual(0, button.expEval("+ 1 + 2 -3"))
        self.assertEqual(6, button.expEval("+ 1 + 2 +3"))
        self.assertEqual(-1, button.expEval("- 5 + 1 + 2 3"))
        self.assertEqual(2, button.expEval("- 1 - 2 3"))
        self.assertEqual(11, button.expEval("- 1 - 10 20"))
        self.assertEqual(12, button.expEval("+ 0 - 1 - 10 + 20 1"))
        self.assertEqual(1000000000000000000, button.expEval("- 1000000000000000000 - \
                                            -1000000000000000000 -1000000000000000000")) #large ints
        with self.assertRaises(AssertionError): #test assert nonempty string
            button.expEval("")
        with self.assertRaises(AssertionError): #test assert type str
            button.expEval(3)

if __name__ == '__main__':
    unittest.main()

