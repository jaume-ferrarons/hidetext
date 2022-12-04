import unittest

from hidetext.textspan import TextSpan
from hidetext.filters import Profanity


class ProfanityTest(unittest.TestCase):
    def test_profanity_works(self):
        detector = Profanity()
        self.assertTrue(detector.is_valid("carallot"))
        self.assertFalse(detector.is_valid("hello"))

    def test_profanity_search(self):
        detector = Profanity()
        profanities = detector.search("No siguis carallot!")
        self.assertListEqual(profanities, [TextSpan(10, 18, "PROFANITY", "carallot")])
        profanities = detector.search("No siguis carallot")
        self.assertListEqual(profanities, [TextSpan(10, 18, "PROFANITY", "carallot")])
        profanities = detector.search("You're so kind!")
        self.assertListEqual(profanities, [])
