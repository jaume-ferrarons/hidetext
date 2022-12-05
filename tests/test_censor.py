import unittest

from hidetext.censor import Censor
from hidetext.textspan import TextSpan
from hidetext import placeholders


class CensorTest(unittest.TestCase):
    def test_censor_char(self) -> None:
        censor = Censor(placeholders.Character())
        text = "Hello this is a beautiful day"
        span = TextSpan(16, 25, "WORD", "beautiful")
        censored_text = censor.censor(text, [span])
        self.assertEqual(censored_text, "Hello this is a ********* day")

    def test_censor_two_spans(self) -> None:
        censor = Censor(placeholders.Character(fixed_length=4))
        text = "Hello this is a beautiful day."
        spans = [TextSpan(16, 25, "WORD", "beautiful"), TextSpan(26, 29, "WORD", "dat")]
        censored_text = censor.censor(text, spans)
        self.assertEqual(censored_text, "Hello this is a **** ****.")

    def test_censor_unordered_spans(self) -> None:
        censor = Censor(placeholders.Character())
        text = "My DNI is 43244328J Email: fdsfsd@gmail.com"
        spans = [
            TextSpan(start=27, end=43, kind="EMAIL", text="fdsfsd@gmail.com"),
            TextSpan(start=10, end=19, kind="ID_CARD", text="43244328J"),
        ]
        censored_text = censor.censor(text, spans)
        self.assertEqual(censored_text, "My DNI is ********* Email: ****************")
