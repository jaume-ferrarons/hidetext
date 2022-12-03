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
