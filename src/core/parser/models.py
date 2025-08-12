from dataclasses import dataclass


@dataclass
class EoraInfo:
    h1: str
    h2: str
    div: str


@dataclass
class EoraInfoJSON:
    idx: int
    category: str
    case_for: str
    title: str
    description: list[str]
