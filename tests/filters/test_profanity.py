import unittest

from hidetext.textspan import TextSpan
from hidetext.filters import Profanity


class ProfanityTest(unittest.TestCase):
    def test_profanity_works(self) -> None:
        detector = Profanity("ca")
        self.assertTrue(detector.is_valid("carallot"))
        self.assertFalse(detector.is_valid("hello"))

    def test_profanity_english(self) -> None:
        detector = Profanity("en")
        self.assertTrue(detector.is_valid("giiiit"))
        self.assertFalse(detector.is_valid("hello"))

    def test_profanity_search(self) -> None:
        detector = Profanity("ca")
        profanities = detector.search("No siguis carallot!")
        self.assertListEqual(profanities, [TextSpan(10, 18, "PROFANITY", "carallot")])
        profanities = detector.search("No siguis carallot")
        self.assertListEqual(profanities, [TextSpan(10, 18, "PROFANITY", "carallot")])
        profanities = detector.search("You're so kind!")
        self.assertListEqual(profanities, [])

    def test_profanity_word_normalization(self) -> None:
        detector = Profanity("ca")
        self.assertTrue(detector.is_valid("Pinxo"))
        self.assertTrue(detector.is_valid("PINXO"))
        self.assertTrue(detector.is_valid("pinxo"))
        self.assertFalse(detector.is_valid("hello"))
        self.assertTrue(detector.is_valid("piiinxo"))
        self.assertTrue(detector.is_valid("caralllllooOot"))

    def test_profanity_search_normalization(self) -> None:
        detector = Profanity("ca")
        profanities = detector.search("No siguis CARALLOOOT!")
        self.assertListEqual(profanities, [TextSpan(10, 20, "PROFANITY", "CARALLOOOT")])

    def test_word_normalization(self) -> None:
        detector = Profanity()
        self.assertEqual(detector._normalize_word("hoooola"), "hola")
        self.assertEqual(detector._normalize_word("hoOoLa"), "hola")
        self.assertEqual(detector._normalize_word("carallloooot"), "carallot")
        self.assertEqual(detector._normalize_word("rrrrr"), "rr")
