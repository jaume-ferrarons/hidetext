import unittest

from hidetext.textspan import TextSpan
from hidetext.placeholders import Kind


class KindTest(unittest.TestCase):
    def test_basic_kind(self):
        placeholder = Kind()
        span = TextSpan(16, 25, "WORD", "beautiful")
        replacement = placeholder.replace(span)
        self.assertEqual(replacement, "<WORD>")

    def test_different_characters(self):
        placeholder = Kind(start_character="(", end_character=")")
        span = TextSpan(16, 25, "HAPPY", "beautiful")
        replacement = placeholder.replace(span)
        self.assertEqual(replacement, "(HAPPY)")
