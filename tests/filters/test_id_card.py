import unittest

from hidetext.filters import IdCard
from hidetext.textspan import TextSpan


class IdCardTest(unittest.TestCase):
    def test_basic_dni(self):
        filter = IdCard()
        dnis = filter.search("12345678J")
        self.assertListEqual(dnis, [TextSpan(0, 9, "ID_CARD", "12345678J")])

    def test_basic_nie(self):
        filter = IdCard()
        dnis = filter.search("X0523821F")
        self.assertListEqual(dnis, [TextSpan(0, 9, "ID_CARD", "X0523821F")])
