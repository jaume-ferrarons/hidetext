import unittest

from hidetext.textspan import TextSpan


class TextSpanTest(unittest.TestCase):
    def test_textspan_length(self):
        span = TextSpan(0, 4, "PERSON", "John")
        self.assertEqual(span.length, 4)
