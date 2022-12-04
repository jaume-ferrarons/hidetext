import itertools
from typing import List
from .filters.filter import Filter
from .filters import Email, Phone, Profanity, IdCard
from .censor import Censor


class Hidetext:
    filters: List[Filter] = [Email(), Phone(), Profanity(), IdCard()]

    def hide(self, text: str):
        spans = list(
            itertools.chain.from_iterable([f.search(text) for f in self.filters])
        )
        censor = Censor()
        return censor.censor(text, spans)
