import unittest

from hidetext import Hidetext


class HidetextTest(unittest.TestCase):
    def test_basic_hide(self):
        hide = Hidetext()
        cleaned = hide.hide("No siguis carallot!")
        self.assertEqual(cleaned, "No siguis ********!")
