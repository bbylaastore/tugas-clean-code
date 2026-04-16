import unittest
from calculator import hitung_diskon

class TestDiskon(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(hitung_diskon(100000, 10, False), 90000)

    def test_bonus(self):
        self.assertEqual(hitung_diskon(100000, 10, True), 100000)

    def test_batas(self):
        self.assertEqual(hitung_diskon(200000, 0, True), 100000)

if __name__ == "__main__":
    unittest.main()