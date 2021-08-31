import random
import unittest
from challenge import DataCapture


class TestDataCaptureStats(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capture = DataCapture()
        items = [0, 1, 1, 1, 4, 4, 7, 9, 17, 24, 37, 37, 81, 121,
                 125, 130, 150, 191, 521, 921, 931, 931, 931, 999]
        random.shuffle(items)
        for i in items:
            self.capture.add(i)

        self.stats = self.capture.build_stats()

    def test_less(self):
        self.assertEqual(bool(self.stats), True)
        self.assertEqual(self.stats.less(4), 4)
        self.assertEqual(self.stats.less(81), 12)
        self.assertEqual(self.stats.less(170), 17)
        self.assertEqual(self.stats.less(900), 19)
        self.assertEqual(self.stats.less(0), 0)

    def test_between(self):
        self.assertEqual(bool(self.stats), True)
        self.assertEqual(self.stats.between(2, 9), 4)
        self.assertEqual(self.stats.between(5, 900), 13)
        self.assertEqual(self.stats.between(17, 191), 10)
        self.assertEqual(self.stats.between(37, 999), 14)

    def test_greater(self):
        self.assertEqual(bool(self.stats), True)
        self.assertEqual(self.stats.greater(900), 5)
        self.assertEqual(self.stats.greater(121), 10)
        self.assertEqual(self.stats.greater(500), 6)
        self.assertEqual(self.stats.greater(999), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
