import unittest

from hidetext.textspan import TextSpan
from hidetext.placeholders import Character


class CharacterTest(unittest.TestCase):
    def test_basic_character(self) -> None:
        placeholder = Character()
        span = TextSpan(16, 25, "WORD", "beautiful")
        replacement = placeholder.replace(span)
        self.assertEqual(replacement, "*********")

    def test_different_character(self) -> None:
        placeholder = Character(character="$")
        span = TextSpan(16, 25, "WORD", "beautiful")
        replacement = placeholder.replace(span)
        self.assertEqual(replacement, "$$$$$$$$$")

    def test_fixed_length(self) -> None:
        placeholder = Character(character="$", fixed_length=2)
        span = TextSpan(16, 25, "WORD", "beautiful")
        replacement = placeholder.replace(span)
        self.assertEqual(replacement, "$$")
