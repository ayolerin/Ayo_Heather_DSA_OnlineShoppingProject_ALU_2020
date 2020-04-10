# author Ayo
# this is where we are importing our file
import sys
from io import StringIO
# from Main_File_Owner_Class import *
from Main_File_Clothes_Functions import *
from Clothes_Class import *
import unittest

# this is where we are testing our init for our Clothes
class TestStringMethod(unittest.TestCase):
    def test__init__Clothes(self):
        Clothes7 =Clothes("Cap", "Pink", "$5", "small")
        self.assertEqual(Clothes7.color, "Pink")
    # this is where we are testing our str for our Clothes

    def test__str__Clothes(self):
        Clothes_type = "Cap"
        color = "pink"
        self.assertEqual(' Your Clothes type:' + Clothes_type + ' ' + 'Color: ' + color)

    def testUppercase(self):
            self.assertEqual('cap'.upper(), 'CAP')

    def testremoveClothes(self):
        ask = 'CAP'.lower()
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        new_owner.remove(new_owner,ask)
        self.assertEqual(capturedOutput.getvalue(), "You have removed a cap from your Clothes list\n")

    def testbookClothes(self):
        a = 1
        b = 3
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        new_customer.book_flight(a,b,new_customer)
        self.assertEqual(capturedOutput.getvalue(), "You have bought a first class ticket to Kigali\n")


# this finishes our test
if __name__ == '__main__':
    unittest.main()