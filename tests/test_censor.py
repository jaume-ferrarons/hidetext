import unittest

from hidetext.censor import Censor
from hidetext.textspan import TextSpan


class CensorTest(unittest.TestCase):
    def test_censor_char(self):
        censor = Censor()
        text = "Hello this is a beautiful day"
        span = TextSpan(16, 25, "WORD", "beautiful")
        censored_text = censor.censor(text, [span])
        self.assertEqual(censored_text, "Hello this is a ********* day")

        censor = Censor(censor_char="$")
        censored_text = censor.censor(text, [span])
        self.assertEqual(censored_text, "Hello this is a $$$$$$$$$ day")

    def test_censor_fixed_length(self):
        censor = Censor(fixed_length=4)
        text = "Hello this is a beautiful day"
        span = TextSpan(16, 25, "WORD", "beautiful")
        censored_text = censor.censor(text, [span])
        self.assertEqual(censored_text, "Hello this is a **** day")

    def test_censor_fixed_length_2(self):
        censor = Censor(fixed_length=4)
        text = "Hello this is a beautiful day."
        spans = [TextSpan(16, 25, "WORD", "beautiful"), TextSpan(26, 29, "WORD", "dat")]
        censored_text = censor.censor(text, spans)
        self.assertEqual(censored_text, "Hello this is a **** ****.")
