import unittest

from .find_clump import find_clump
from .frequent_words import frequent_words


class TestChapter1(unittest.TestCase):

    def test_find_clump(self):
        self.assertListEqual(find_clump('AAAACGTCGAAAAA', 2, 4, 2), ['AA'])
        self.assertListEqual(sorted(find_clump('ACGTACGT', 1, 5, 2)), ['A', 'C', 'G', 'T'])

    def test_frequent_words(self):
        self.assertListEqual(frequent_words('ACAACTATGCATCACTATCGGGAACTATCCT', 5), ['ACTAT'])
        self.assertListEqual(frequent_words('CGATATATCCATAG', 3), ['ATA'])
        self.assertListEqual(sorted(frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), ['CATG', 'GCAT'])
