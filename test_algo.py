import sys
import unittest
from algo import f

class TestFunction(unittest.TestCase):
    
    a = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]

    def test_empty_array(self):
        self.assertEqual(f([],12), -1)
    
    def test_null_array(self):
        self.assertEqual(f(None,12), -1)

    def test_not_array(self):
        self.assertEqual(f('1, 2, 3, 4',2), -1)
    
    def test_target_is_negative(self):
        self.assertEqual(f(self.a,-1), -1)

    def test_target_less_than_min(self):
        self.assertEqual(f(self.a,2), -1)

    def test_target_float_less_than_min(self):
        self.assertEqual(f(self.a,2.9), -1)
    
    def test_target_is_min(self):
        self.assertEqual(f(self.a,3), 3)
    
    def test_target_is_greater_than_max(self):
        self.assertEqual(f(self.a,22), 21)
    
    def test_target_exists(self):
        self.assertEqual(f(self.a,12), 12)

    def test_next_smallest_value(self):
        self.assertEqual(f(self.a,13), 12)

    def test_target_is_max_int(self):
        self.assertEqual(f(self.a,sys.maxsize), 21)

    b = [-1000, -500, 0, 1000]

    def test_next_smallest_value2(self):
        self.assertEqual(f(self.b,-501), -1000)

    def test_target_less_than_min2(self):
        self.assertEqual(f(self.b,-1001), -1)
    
    def test_next_smallest_value3(self):
        self.assertEqual(f(self.b,-499), -500)

    def test_next_smallest_value4(self):
        self.assertEqual(f(self.b,1001), 1000)

if __name__ == '__main__':
    unittest.main()