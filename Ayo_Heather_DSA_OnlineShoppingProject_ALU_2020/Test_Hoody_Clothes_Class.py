# author Heather
# this is where we are importing our file
import sys
from io import StringIO
from Main_File_Clothes_Functions import *
import unittest
from Hoody_Clothes_Class import *

# this is where we test for hoody class
hoody1 = Hoody_Clothes("Hoody","pink","$20","small")
hoody1.__str__()
# this is where we are testing our init for our hoody class
class TestStringMethod(unittest.TestCase):

    def test__init__hoody_class(self):
            hoody1 = Hoody_Clothes("Hoody", "blue", "$20", "large")
            self.assertEqual(hoody1.color, "Hooody")
    # this is where we are testing our str for hoody class
    def test__str__hoody(self):
            clothes_type = "Hoody"
            color = "Black"
            print(' Your Clothes type:' + clothes_type + ' ' + 'Color: ' + color)

    def testUppercase(self):
            self.assertEqual('hoody'.upper(), 'HOODY')

    def testremoveHoody(self):
        ask = 'HOODY'.lower()
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        new_owner.remove(clothes_list)
        self.assertEqual(capturedOutput.getvalue(), "You have removed a hoody from your clothes list\n")



# this finishes our test
if __name__ == '__main__':
    unittest.main()