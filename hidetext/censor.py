from typing import List, Optional

from .textspan import TextSpan


class Censor:
    def __init__(self, censor_char: str = "*", fixed_length: Optional[int] = None):
        self._censor_char = censor_char
        self._fixed_length = fixed_length

    def censor(self, text: str, spans: List[TextSpan]) -> str:
        censored_text = []
        last_end = 0
        for span in spans:
            censored_text.append(text[last_end : span.start])
            replacement_length = (
                self._fixed_length if self._fixed_length else span.length
            )
            replacement = self._censor_char * replacement_length
            censored_text.append(replacement)
            last_end = span.end
        censored_text.append(text[last_end:])
        return "".join(censored_text)
