# author Ayo
# this is where we import our file
from Main_File_Owner_Class import *
import unittest
from Caps_Clothes_class import *
from Main_File_Clothes_Functions import *
# this is where we test for owner

# this is where we are testing our view  function
class TestStringMethods(unittest.TestCase):
    def testview_owner(self):
            clothes_list = []
            clothes1 = Caps_Clothes("Cap", "yellow", "$5", "small")
            clothes_list.append(clothes1)
            size_before = len(clothes_list)
            OwnerHeather = Owner("Heather", "Mataruse", 1234)
            OwnerHeather.view(clothes_list, new_owner)
            size_after = len(clothes_list)
            self.assertEqual(size_after, size_before)

    # this finishes our test
    # this is where we are testing our menu owner function
    def testmenu_owner(self):
            print("Enter 1 to add a product\n"
                  "Enter 2 to remove a product\n"
                  "Enter 3 to view all products\n")
    # this is where we are testing our info owner function

    # this is where we are testing our remove a product
    def testremove(self):
            clothes_list = []
            clothes1 = Caps_Clothes("Commercial clothes", "BMW", "A1B2C3D4", "1220")
            clothes_list.append(clothes1)
            size_before = len(clothes_list)
            OwnerHeather = Owner("Heather", "Mataruse", 1234)
            clothes_list.remove(clothes1)
            OwnerHeather.remove(clothes_list, new_owner)
            size_after = len(clothes_list)
            self.assertEqual(size_after, size_before - 1)
    # this is where we are testing our str for our owner
    def test__str__owner(self):
            f_name = "Heather"
            l_name = "Mataruse"
            pno = "Ao0dhd"
            print('\nYour first name is :', f_name,
                      "\nYour last name is: ", l_name,
                      "\nYour password is :" + pno)
    # this is where we are testing our init for our owner
    def test_init_owner(self):
            person1 = Owner("Ayo", "Heather", "A1234")
            self.assertEqual(person1.last_name, "Heather")


    def testadd(self):
        clothes_list = []
        clothes2 = Caps_Clothes("Cap", "white", "$5", 'small')
        clothes_list.append(clothes2)
        clothes1 = Caps_Clothes("Cap", "blue", "$5", "large")
        clothes_list.append(clothes1)

        size_before = len(clothes_list)

        OwnerHeather = Owner("Heather", "Mataruse", 1234)
        OwnerHeather.add(clothes_list, new_owner)
        size_after = len(clothes_list)
        self.assertEqual(size_after, size_before + 1)
# this finishes our test
if __name__ == '__main__':
    unittest.main()