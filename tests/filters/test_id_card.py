import unittest

from hidetext.filters import IdCard
from hidetext.textspan import TextSpan


class IdCardTest(unittest.TestCase):
    def test_basic_dni(self) -> None:
        filter = IdCard()
        dnis = filter.search("12345678J")
        self.assertListEqual(dnis, [TextSpan(0, 9, "ID_CARD", "12345678J")])

    def test_basic_nie(self) -> None:
        filter = IdCard()
        dnis = filter.search("X0523821F")
        self.assertListEqual(dnis, [TextSpan(0, 9, "ID_CARD", "X0523821F")])

    def test_no_dni_search(self) -> None:
        filter = IdCard()
        dnis = filter.search("12345678JA")
        self.assertListEqual(dnis, [])
