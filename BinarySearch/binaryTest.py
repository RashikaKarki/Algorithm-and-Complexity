import unittest
from binary import binary_search

class TestSearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 4,5, 6, 7, 8]
        self.assertEqual(binary_search(data,0,7, 6), 5)

    def test_searchChar(self):
        data = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(binary_search(data, 0,4,'e'), 4)

if __name__ == "__main__":
    unittest.main()
