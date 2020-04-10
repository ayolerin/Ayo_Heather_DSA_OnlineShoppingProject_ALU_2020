# author heather
# this is where we import our file
import PyPDF2
import docx
from Main_File_Customer_Class import *
import unittest
from Caps_Clothes_class import *
from Hoody_Clothes_Class import *


class TestStringMethods(unittest.TestCase):

    # this is where we are testing our init for our customer
    def test_init_customer(self):
        person1 = Customer("Ella", "Adams", "A234")
        self.assertEqual(person1.last_name, "Adams")

        # this is where we are testing our str for our customer

    def test__str__customer(self):
        f_name = "Heather"
        l_name = "Mataruse"
        pno = "Ao0dhd"
        print('\nYour first name is :', f_name,
              "\nYour last name is: ", l_name,
              "\nYour password is :" + pno)

        # this is where we are testing our view customer function

    def testview_customer(self):
        clothes_list = []
        clothes1 = Caps_Clothes("Cap", "blue", "$5", "small")
        clothes2 = Caps_Clothes("Cap", "red", "$5", "medium")
        clothes_list.append(clothes1)
        clothes_list.append(clothes2)
        size_before = len(clothes_list)
        CustomerImali = Customer('Ayo', 'Fisher', 4567)
        CustomerImali.view(clothes_list)
        size_after = len(clothes_list)
        self.assertEqual(size_after, size_before)

        # this is where we are testing our buy function

    def testbuy(self):
        hoody_list = []
        hoody1 = Hoody_Clothes("Hoody", "white", "$20", "medium")
        hoody2 = Hoody_Clothes("Hoody", "black", "$20", "small")
        hoody_list.append(hoody1)
        hoody_list.append(hoody2)
        size_before = len(hoody_list)
        CustomerHeather = Customer("Heather", "Mataruse", "AE2308")

        CustomerHeather.buy()
        size_after = len(hoody_list)
        self.assertEqual(size_after, size_before)




# this finishes our test
if __name__ == '__main__':
    unittest.main()
