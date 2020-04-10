# author Ayo
# this is where we are importing our file
import sys
from io import StringIO
import unittest
from Caps_Clothes_class import *
from Main_File_Clothes_Functions import *


class TestStringMethods(unittest.TestCase):
    # this is where we are testing our init for our Caps Clothes

    def test__init__Caps_Clothes(self):
        Caps_Clothes1 = Caps_Clothes("Cap", "White", "$5", "large")
        self.assertEqual(Caps_Clothes1.color, "White")

    # this is where we are testing our str for our caps class
    def test__str__Caps_Clothes(self):
        Clothes_type = "Cap"
        color = "orange"
        print(' Your Clothes type:' + Clothes_type + ' ' + 'Color: ' + color)

    def testUppercase(self):
        self.assertEqual('caps clothes'.upper(), 'CAPS CLOTHES')

    def testremoveCapsClothes(self, new_owner, Clothes_list):
        ask = 'cap'.lower()
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        new_owner.remove(Clothes_list)
        self.assertEqual(capturedOutput.getvalue(), "You have removed a cap from your Clothes list\n")



# this finishes our test
if __name__ == '__main__':
    unittest.main()
