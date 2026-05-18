from dataclasses import dataclass


@dataclass
class Object:
    name: str
    id: int
    typ: str
    price: int
    desc: str
