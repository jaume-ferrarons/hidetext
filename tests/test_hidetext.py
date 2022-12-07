import unittest

from hidetext import Hidetext


class HidetextTest(unittest.TestCase):
    def test_basic_character(self) -> None:
        hide = Hidetext("ca")
        cleaned = hide.character("No siguis carallot!")
        self.assertEqual(cleaned, "No siguis ********!")

    def test_basic_character_2(self) -> None:
        hide = Hidetext()
        cleaned = hide.character("This is may email: 1234@gmal.com")
        self.assertEqual(cleaned, "This is may email: *************")

    def test_basic_kind(self) -> None:
        hide = Hidetext()
        cleaned = hide.kind(
            "This is may email: 1234@gmal.com", start_character="(", end_character=")"
        )
        self.assertEqual(cleaned, "This is may email: (EMAIL)")
