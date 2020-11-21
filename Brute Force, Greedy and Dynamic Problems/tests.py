import unittest
from greedy import greedy
from bruteforce import bruteforce, get_strings
from dynamic import dynamic
from greedy import greedy

class TestStringMethods(unittest.TestCase):

    def test_bruteforce(self):
        self.assertEqual(get_strings(1),['0','1'])
        with self.assertRaises(Exception):
            bruteforce([1,2], [1], 2)
        self.assertEqual(bruteforce([1,2,3], [4, 5, 1], 4), 3)
        self.assertEqual(bruteforce([1,2,3], [4, 5, 6], 3), 0)

    def test_greedy(self):
        with self.assertRaises(Exception):
            greedy([1,2], [1], 2)
        self.assertEqual(greedy([60, 100, 120] , [10, 20, 30] , 50), 240)

    def test_dynamic(self):
        with self.assertRaises(Exception):
            dynamic([1,2], [1], 2)
        self.assertEqual(dynamic([60, 100, 120] , [10, 20, 30] , 50), 220)
        self.assertEqual(dynamic([1,2,3], [4, 5, 6], 3), 0)
        self.assertEqual(dynamic([1,2,3], [4, 5, 1], 4), 3)
    
if __name__ == "__main__":
    unittest.main() 