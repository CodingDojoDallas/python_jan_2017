import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
    def testMap(self):
        self.test_list = [1,2,3,4]
        self.map_result = self._.map(self.test_list, lambda x: x**2)
        return self.assertEqual([1,4,9,16], self.test_list)
    def testReduce(self):
        self.test_list = [1,2,3,4]
        self.reduce_result = self._.reduce(self.test_list, lambda x, y: x*y, 1)
        return self.assertEqual(24, self.reduce_result)
    def testFind(self):
        self.test_list = [1,2,3,4,5,6]
        self.find_result = self._.find(self.test_list, lambda x: x > 3)
        self.assertEqual(4, self.find_result)
    def testFilter(self):
        self.test_list = [1,2,3,4,5,6,7,8,9,10]
        self.filter_result = self._.filter(self.test_list, lambda x: x > 6)
        self.assertEqual([7,8,9,10], self.filter_result)
    def testReject(self):
        self.test_list = [1,2,3,4,5]
        self.reject_result = self._.reject(self.test_list, lambda x: x == 3)
        self.assertEqual([1,2,4,5], self.reject_result)

if __name__ == "__main__":
    unittest.main()