import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """raise ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter_empty(self):
        """returns None when list is empty"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
    def test_max_list_iter_mult_numbers_equal(self):
        """tests function when the max number appears more than once"""
        tlist = [5, 5, 1, 4]
        self.assertEqual(max_list_iter(tlist), 5)
    def test_max_list_iter_all_equal(self):
        """tests function when all numbers in list are the same"""
        tlist = [8, 8, 8]
        self.assertEqual(max_list_iter(tlist), 8)
    def test_max_list_iter_neg_num(self):
        """tests function when the list contains negative numbers"""
        tlist = [0, -8, 12]
        self.assertEqual(max_list_iter(tlist), 12)



    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        int_list = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(int_list)
        
        int_list = [3, 2, 1]
        self.assertEqual(reverse_rec(int_list, [1, 2, 3]))

        int_list = [4, 1, 0]
        self.assertEqual(reverse_rec(int_list, [0, 1, 4]))

        int_list = []
        self.assertEqual(reverse_rec(int_list, []))

        int_list = [9]
        self.assertEqual(reverse_rec(int_list, [9]))

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
