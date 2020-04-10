import sys
from io import StringIO
import unittest
from Main_File_Owner_Class import *
from Main_File_Customer_Class import *

    # this is where we are testing our init for our cropTop clothes
class TestStringMethod(unittest.TestCase):
    def test__init__cropTop_clothes(self):
        clothes1 = CropTop_Clothes('Crop Top ', 'White', '$10', 'medium')
        self.assertEqual(clothes1.color, "White")

        # this is where we are testing our str for our cropTop clothes

    def test__str__cropTop_clothes(self):
        clothes_type = "Crop top"
        color = "Black"
        print(' Your Clothes Type:' + clothes_type + ' ' + 'Color: ' + color)

    def testcropTop(self):
        cropTop_list = []
        CropTop1 = ("Black crop top")
        CropTop2 = ("White crop top")
        cropTop_list.append(CropTop1)
        cropTop_list.append(CropTop2)
        size_before = len(cropTop_list)
        customer_heather = Customer("Heather", "Mataruse", "AE2308")
        cropTop_list.remove(CropTop2)
        customer_heather.cropTop()
        size_after = len(cropTop_list)
        self.assertEqual(size_after, size_before - 1)

    def testUppercase(self):
            self.assertEqual('croptop'.upper(), 'CROPTOP')

    def testremovecropTopclothes(self, new_owner, clothes_list):
        ask = 'Black Crop Top'.lower()
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        new_owner.remove(clothes_list ,ask)
        self.assertEqual(capturedOutput.getvalue(), "You have removed a black crop top from your clothes list\n")


# this finishes our test
if __name__ == '__main__':
    unittest.main()
