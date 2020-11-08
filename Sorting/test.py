import unittest
from main import mergesort, merge, insertionsort

class MergeSortTest(unittest.TestCase):
    def testInt(self):
        data = [90,8,5,1,3]
        output = [1,3,5,8,90]
        data = mergesort(data,0,len(data))
        self.assertEqual(data,output)
   
class InstertionSortTest(unittest.TestCase):
    def testInt(self):
        data = [9,8,5,1,3]
        output = [1,3,5,8,9]
        data = insertionsort(data)
        self.assertEqual(data,output)

if __name__ == "__main__":
    unittest.main()