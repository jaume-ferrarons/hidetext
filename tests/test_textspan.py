import unittest

from hidetext.textspan import TextSpan


class TextSpanTest(unittest.TestCase):
    def test_textspan_length(self) -> None:
        span = TextSpan(0, 4, "PERSON", "John")
        self.assertEqual(span.length, 4)

    def test_textspan_sortable(self) -> None:
        span1 = TextSpan(0, 4, "PERSON", "John")
        span2 = TextSpan(10, 15, "PERSON", "Jimmy")
        self.assertLess(span1, span2)
