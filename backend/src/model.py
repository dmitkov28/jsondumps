from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Source:
    title: str
    date: int
    url: str
    tags: Optional[List[str]] = None
