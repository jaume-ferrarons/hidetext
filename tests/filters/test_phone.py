import unittest

from hidetext.filters import Phone


class EmailTest(unittest.TestCase):
    def test_just_phones(self):
        phone = Phone()
        self.assertTrue(phone.is_valid("+34931234567"))
