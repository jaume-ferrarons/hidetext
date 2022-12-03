from typing import List

from .textspan import TextSpan


class Censor:
    def __init__(self, censor_char: str = "*"):
        self._censor_char = censor_char

    def censor(self, text: str, spans: List[TextSpan]) -> str:
        censored_text = text
        for span in spans:
            text_before = censored_text[: span.start]
            replacement = self._censor_char * span.length
            text_after = censored_text[span.end :]
            censored_text = text_before + replacement + text_after
        return censored_text
