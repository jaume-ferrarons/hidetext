import re
from typing import List

from hidetext.textspan import TextSpan
from .filter import Filter


class Profanity(Filter):
    name: str = "PROFANITY"

    terms = ["carallot", "tanoca"]

    def search(self, text: str) -> List[TextSpan]:
        tokenized = self._tokens(text)
        print(tokenized)
        return [token for token in tokenized if token.text in self.terms]

    def is_valid(self, text: str) -> bool:
        return text in self.terms

    def _tokens(self, text: str) -> List[TextSpan]:
        tokens = []
        last_end = 0
        for match in re.finditer(r"[\s+\!]", text):
            tokens.append(
                TextSpan(
                    last_end, match.start(), self.name, text[last_end : match.start()]
                )
            )
            last_end = match.end()
        if last_end < len(text):
            tokens.append(
                TextSpan(last_end, len(text), self.name, text[last_end : len(text)])
            )
        return tokens
