import unittest

from hidetext.filters.pattern_filter import PatternFilter
from hidetext.textspan import TextSpan


class PatternFilterStub(PatternFilter):
    name = "STUB"

    patterns = {"a": r"[a]+"}


class PatternFilterTest(unittest.TestCase):
    def test_pattern_is_valid(self) -> None:
        stub = PatternFilterStub()
        self.assertTrue(stub.is_valid("aaa"))
        self.assertFalse(stub.is_valid("aaa "))

    def test_pattern_search(self) -> None:
        stub = PatternFilterStub()
        self.assertListEqual(stub.search("bbbb"), [])
        self.assertListEqual(stub.search("bbabb"), [TextSpan(2, 3, "STUB", "a")])
