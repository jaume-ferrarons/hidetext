from dataclasses import dataclass


@dataclass
class TextSpan:
    start: int
    end: int
    kind: str
    text: str

    @property
    def length(self) -> int:
        return self.end - self.start
