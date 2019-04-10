import unittest
from location import *

class TestLab1(unittest.TestCase):
    """Testing the repr function"""
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("SAC", 87.1, 34.1)
        self.assertEqual(repr(loc),"Location('SAC', 87.1, 34.1)")
        loc = Location("NYC", 15.8, 32.9)
        self.assertEqual(repr(loc), "Location('NYC', 15.8, 32.9)")
    """Testing the eq function"""
    def test_eq(self):
        loc1 = Location("OAK", 46.3, 89.0)
        loc2 = Location("OAK", 46.3, 89.0)
        self.assertEqual(loc1, loc2)
        loc1 = Location("SD", 67.4, 132.2)
        loc2 = Location("SD", 67.4, 132.2)
        self.assertEqual(loc1, loc2)
        loc1 = Location("SEA", 75.6, 143.2)
        loc2 = Location("CIN", 45.8, 120.9)
        self.assertNotEqual(loc1, loc2)    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
